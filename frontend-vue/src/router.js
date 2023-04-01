import { createRouter, createWebHistory } from 'vue-router';
import HomePage from './components/HomePage.vue';
import DashboardPage from './components/DashboardPage.vue';
import MachinePage from './components/MachinePage.vue'
import LoginPage from './components/LoginPage.vue'
import UserProfile from '@/components/UserProfile.vue';
import UserManagement from '@/components/UserManagement.vue';
const routes = [
  {
    path: '/',
    name: 'HomePage',
    component: HomePage
  },
  {
    path: '/dashboard',
    name: 'dashboard',
    component: DashboardPage
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

  },
  {
    path: '/UserProfile',
    name: 'UserProfile',
    component: UserProfile,
  },
  {
    path: '/UserManagement',
    name: 'UserManagement',
    component: UserManagement,
  }
  // Add other routes here
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
