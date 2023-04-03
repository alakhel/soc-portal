<template>
    <div>
      <NavBar></NavBar>
  
      <section class="section">
        <div class="container">
          <h1 class="title">Université de Paris-Cité</h1>
          <img src="/public/logo.svg" alt="Université Paris Cité" />
          <p>This is the content of the Portail SOC page.</p>
        </div>
      </section>
    </div>
  </template>
  
  <script>
  import NavBar from './NavBar.vue';
  
  export default {
    components: {
      NavBar,
    },
  };
  </script>
  