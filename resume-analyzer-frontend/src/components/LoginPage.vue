<template>
  <v-container>
    <v-form @submit.prevent="login">
      <v-text-field
        v-model="email"
        label="Email"
        required
      />
      <v-text-field
        v-model="password"
        label="Password"
        type="password"
        required
      />
      <v-btn
        type="submit"
        color="primary"
        class="mt-4"
      >
        Login
      </v-btn>
    </v-form>
  </v-container>
</template>

<script>
import axios from 'axios'

export default {
  name: 'LoginPage',
  data() {
    return {
      email: '',
      password: '',
    }
  },
  methods: {
    async login() {
      try {
        const response = await axios.post('http://127.0.0.1:8081/api/users/login/', {
          email: this.email,
          password: this.password,
        })
        localStorage.setItem('access', response.data.access)
        localStorage.setItem('refresh', response.data.refresh)
        this.$router.push('/')
      } catch (err) {
        alert('Login failed. Please check your credentials.')
      }
    },
  },
}
</script>
