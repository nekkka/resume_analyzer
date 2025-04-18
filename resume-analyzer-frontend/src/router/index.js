import { createRouter, createWebHistory } from 'vue-router'
import LoginPage from '../components/LoginPage.vue'
import RegisterPage from '../components/RegisterPage.vue'
import ResumeUpload from '../components/ResumeUpload.vue'
import JobList from '../components/JobList.vue'
import ResetPassword from '../components/ResetPassword.vue'
import VerifyEmail from '../components/VerifyEmail.vue'
import JobUpload from '../components/JobUpload.vue'



const routes = [
  { path: '/', component: JobList },
  { path: '/login', component: LoginPage },
  { path: '/register', component: RegisterPage },
  { path: '/upload', component: ResumeUpload },
  { path: '/reset-password', component: ResetPassword },
  { path: '/verify-email', component: VerifyEmail },
  { path: '/post-job', component: JobUpload },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
