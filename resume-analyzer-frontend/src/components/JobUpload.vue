<template>
    <v-container>
      <v-form @submit.prevent="postJob">
        <v-text-field v-model="title" label="Job Title" required />
        <v-text-field v-model="description" label="Job Description" required />
        <v-btn type="submit" color="primary">Post Job</v-btn>
      </v-form>
    </v-container>
  </template>
  
  <script>
  import axios from 'axios'
  
  export default {
    data() {
      return {
        title: '',
        description: '',
      }
    },
    methods: {
      async postJob() {
        try {
          await axios.post('http://localhost:8000/api/jobs/create/', {
            title: this.title,
            description: this.description,
          })
          alert('Job posted successfully!')
        } catch (error) {
          alert('Failed to post job.')
        }
      },
    },
  }
  </script>
  