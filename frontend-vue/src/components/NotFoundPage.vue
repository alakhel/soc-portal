<!-- ./components/NotFoundPage.vue -->
<template>
    <div class="not-found">
      <h1>404: Page Not Found</h1>
      <p>Sorry, the page you're looking for cannot be found.</p>
      <router-link to="/">Return to Home</router-link>
    </div>
  </template>
  
  <script>
  export default {
    name: "NotFoundPage"
  };
  </script>
  
  <style scoped>
  .not-found {
    text-align: center;
  }
  </style>
  