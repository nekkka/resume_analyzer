<template>
  <v-container>
    <v-form @submit.prevent="register">
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
      <v-text-field
        v-model="confirmPassword"
        label="Confirm Password"
        type="password"
        required
      />
      <v-btn
        type="submit"
        color="primary"
        class="mt-4"
      >
        Register
      </v-btn>
    </v-form>
  </v-container>
</template>

<script>
import axios from 'axios'

export default {
  name: 'RegisterPage',
  data() {
    return {
      email: '',
      password: '',
      confirmPassword: '',
    }
  },
  methods: {
    async register() {
      if (this.password !== this.confirmPassword) {
        alert("Passwords do not match")
        return
      }
      try {
        await axios.post('http://127.0.0.1:8081/api/users/register/', {
          email: this.email,
          password: this.password,
        })
        alert('Registration successful! Please check your email to verify your account.')
        this.$router.push('/login')
      } catch (err) {
        alert('Registration failed. Please try again.')
      }
    },
  },
}
</script>
