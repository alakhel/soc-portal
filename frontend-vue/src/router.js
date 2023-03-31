import { createRouter, createWebHistory } from 'vue-router';
import HomePage from './components/HomePage.vue';
import MachinePage from './components/MachinePage.vue'
import LoginPage from './components/LoginPage.vue'

const routes = [
  {
    path: '/',
    name: 'HomePage',
    component: HomePage
  },
  {
    path: "/Machine",
    name:"Machine",
    component: MachinePage

  },
  {
    path: "/login",
    name:"login",
    component: LoginPage

  }
  // Add other routes here
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
