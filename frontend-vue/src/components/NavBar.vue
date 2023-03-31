<template>
    <nav class="navbar" role="navigation" aria-label="main navigation">
      <div class="navbar-brand">
        <a class="navbar-item" href="/">
            <img src="@/assets/logo-nav.svg"/>
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
          <a class="navbar-item" href="/">Home</a>
  
          <a class="navbar-item" href="/machine">Machine</a>
        </div>
  
        <div class="navbar-end">
          <div class="navbar-item">
            <div class="buttons">
              <a class="button is-light" href="/login">Log in</a>
            </div>
          </div>
        </div>
      </div>
    </nav>
  </template>
  
  <script>
  export default {
    data() {
      return {
        burgerActive: false,
      };
    },
    methods: {
      toggleBurger() {
        this.burgerActive = !this.burgerActive;
      },
    },
  };
  </script>
  