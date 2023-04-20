<template>
  <nav class="navbar" role="navigation" aria-label="main navigation">
    <div class="navbar-brand">
      <a class="navbar-item" href="/">
        <img src="@/assets/logo-nav.svg" />
      </a>

      <a
        role="button"
        class="navbar-burger"
        aria-label="menu"
        aria-expanded="false"
        data-target="navbarBasicExample"
        @click="toggleBurger"
      >
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
      </a>
    </div>

    <div :class="{'navbar-menu': true, 'is-active': burgerActive}" id="navbarBasicExample">
      <div class="navbar-start">
        <router-link class="navbar-item" to="/">Home</router-link>
        <router-link v-if="isAuth" class="navbar-item" to="/dashboard">Dashboard</router-link>
        <router-link v-if="isAuth && isAdminUser" class="navbar-item" to="/machine">Machine</router-link>
        <router-link v-if="isAuth && isAdminUser" class="navbar-item" to="/UserManagement">User Management</router-link>
      </div>

      <div class="navbar-end">
        <div  class="navbar-item">
          <router-link v-if="isAuth" class="navbar-item" to="/UserProfile">
            <img class="user-icon" src="@/assets/profile.png" alt="My Profile" />
          </router-link>

          <div class="buttons">
            <router-link v-if="!isAuth" class="button is-light" to="/login">Log in</router-link>
            <button v-else class="button is-light" @click="logout">Log out</button>
          </div>
        </div>
      </div>
    </div>
  </nav>
</template>

<script>
import { isAuth, logout, isAdmin } from "@/services/authService";

export default {
  data() {
    return {
      burgerActive: false,
      isAuth: isAuth(),
    };
  },
  computed: {
  isAdminUser() {
    return isAdmin();
  },
},

  methods: {
    toggleBurger() {
      this.burgerActive = !this.burgerActive;
    },
    logout() {
      logout();
      this.isAuth = false;
      this.$router.push("/login");
    },
  },
};
</script>
<style>
  .user-icon {
    max-height: 2.5rem; /* Adjust the value to fit the icon within your navbar */
    vertical-align: middle;
  }
</style>
