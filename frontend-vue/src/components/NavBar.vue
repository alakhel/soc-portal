<template>
    <nav class="navbar" role="navigation" aria-label="main navigation">
      <div class="navbar-brand">
        <a class="navbar-item" href="#">
          <img src="/public/logonav.svg" width="112" height="28" />
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
          <a class="navbar-item">Home</a>
  
          <a class="navbar-item">Project</a>
  
          <div class="navbar-item has-dropdown is-hoverable">
            <a class="navbar-link">Equipes</a>
  
            <div class="navbar-dropdown">
              <a class="navbar-item">SOC 1</a>
              <a class="navbar-item">SOC 2</a>
              <a class="navbar-item">SOC 3</a>
              <a class="navbar-item">Admin</a>
              <a class="navbar-item">Pentest & Web</a>
              <hr class="navbar-divider" />
              <a class="navbar-item">Raise a ticket for pentest</a>
            </div>
          </div>
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
  