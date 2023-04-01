<template>
    <div>
      <NavBar></NavBar>
  
          <img src="@/assets/logo.svg" alt="Université Paris Cité" class="banner"/>
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
<style>
.banner {
  width: 100%;
  height: 100%;
}
</style>
  