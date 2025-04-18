<!-- src/components/ResumeUpload.vue -->
<template>
    <v-container>
      <v-file-input v-model="file" label="Choose resume file" accept=".pdf,.doc,.docx" />
      <v-btn color="primary" @click="upload">Upload</v-btn>
    </v-container>
  </template>
  
  <script>
  import axios from 'axios'
  
  export default {
    data() {
      return {
        file: null,
      }
    },
    methods: {
      async upload() {
        const formData = new FormData()
        formData.append('resume', this.file)
  
        try {
          const token = localStorage.getItem('access')
          await axios.post('http://127.0.0.1:8081//resume/upload/', formData, {
            headers: {
              'Authorization': `Bearer ${token}`,
              'Content-Type': 'multipart/form-data',
            },
          })
          alert('Uploaded!')
        } catch (err) {
          alert('Upload failed')
        }
      },
    },
  }
  </script>
  