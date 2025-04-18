<template>
    <v-container>
      <v-form @submit.prevent="requestReset">
        <v-text-field v-model="email" label="Email" required />
        <v-btn type="submit" color="primary">Request Password Reset</v-btn>
      </v-form>
    </v-container>
  </template>
  
  <script>
  import axios from 'axios'
  
  export default {
    data() {
      return {
        email: '',
      }
    },
    methods: {
      async requestReset() {
        try {
          await axios.post('http://127.0.0.1:8081/api/users/request-password-reset/', {
            email: this.email,
          })
          alert('Check your email for reset instructions.')
        } catch (error) {
          alert('Failed to send reset link.')
        }
      },
    },
  }
  </script>
  