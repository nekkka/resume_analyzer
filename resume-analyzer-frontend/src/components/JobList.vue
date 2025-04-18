<!-- src/components/JobList.vue -->
<template>
    <v-container>
      <v-btn @click="getJobs">Get Jobs</v-btn>
      <v-list>
        <v-list-item v-for="job in jobs" :key="job.id" :title="job.title" />
      </v-list>
    </v-container>
  </template>
  
  <script>
  import axios from 'axios'
  
  export default {
    data() {
      return {
        jobs: [],
      }
    },
    methods: {
      async getJobs() {
        const res = await axios.get('http://127.0.0.1:8081/api/jobs/')
        this.jobs = res.data
      },
    },
  }
  </script>
  