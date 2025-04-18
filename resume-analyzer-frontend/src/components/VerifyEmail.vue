<template>
    <v-container>
      <v-form @submit.prevent="verifyEmail">
        <v-text-field v-model="token" label="Verification Token" required />
        <v-btn type="submit" color="primary">Verify Email</v-btn>
      </v-form>
    </v-container>
  </template>
  
  <script>
  import axios from 'axios'
  
  export default {
    data() {
      return {
        token: '',
      }
    },
    methods: {
      async verifyEmail() {
        try {
          await axios.get(`http://127.0.0.1:8081/api/users/verify-email/?token=${this.token}`)
          alert('Email successfully verified!')
        } catch (error) {
          alert('Failed to verify email.')
        }
      },
    },
  }
  </script>
  