import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import RegistroView from '../views/RegistroView.vue'

const routes = [
  { path: '/', name: 'home', component: HomeView },
  { path: '/registro', name: 'registro', component: RegistroView }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router