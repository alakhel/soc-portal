import { createRouter, createWebHistory } from 'vue-router';
import HomePage from './components/HomePage.vue';
import DashboardPage from './components/DashboardPage.vue';
import MachinePage from './components/MachinePage.vue'
import LoginPage from './components/LoginPage.vue'
import UserProfile from '@/components/UserProfile.vue';
import UserManagement from '@/components/UserManagement.vue';
import { isAuth, isAdmin } from "@/services/authService";

const routes = [
  {
    path: '/',
    name: 'HomePage',
    component: HomePage
  },
  {
    path: '/dashboard',
    name: 'dashboard',
    component: DashboardPage,
    meta: { requiresAuth: true },

  },
  {
    path: "/Machine",
    name:"Machine",
    component: MachinePage,
    meta: { requiresAuth: true },
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
    meta: { requiresAuth: true },

  },
  {
    path: '/UserManagement',
    name: 'UserManagement',
    component: UserManagement,
    meta: { requiresAuth: true, requiresAdmin: true }, // Add requiresAdmin

  }
  // Add other routes here
];
const router = createRouter({
  history: createWebHistory(),
  routes,
});
router.beforeEach((to, from, next) => {
  const isUserAdmin = isAdmin(); // Get the admin status

  if (to.matched.some((record) => record.meta.requiresAuth)) {
    if (isAuth()) {
      if (to.matched.some((record) => record.meta.requiresAdmin) && !isUserAdmin) {
        next({ path: '/dashboard' });
      } else {
        next();
      }
    } else {
      next({
        path: "/login",
        query: { redirect: to.fullPath },
      });
    }
  } else {
    next();
  }
});



export default router;
