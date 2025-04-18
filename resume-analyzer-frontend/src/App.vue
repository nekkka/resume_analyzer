<template>
  <v-app>
    <v-app-bar app color="primary" dark>
      <v-toolbar-title>Resume Analyzer</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn text to="/">Jobs</v-btn>
      <v-btn text to="/upload">Upload Resume</v-btn>
      <v-btn text to="/login">Login</v-btn>
      <v-btn text to="/register">Register</v-btn>
      <v-btn text to="/reset-password">Reset Password</v-btn>
      <v-btn text to="/verify-email">Verify Email</v-btn>
      <v-btn text to="/post-job">Post Job</v-btn>
    </v-app-bar>

    <v-main>
      <v-container class="mt-5">
        <router-view />
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: 'App',
}
</script>

<style>
body {
  margin: 0;
}
</style>
