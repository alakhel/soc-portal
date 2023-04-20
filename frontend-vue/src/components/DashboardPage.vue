<template>
    <div>
      <NavBar></NavBar>
      <h1>Dashboard</h1>
      <div class="container">
    <div class="columns is-multiline">
      <div class="column is-one-third" v-for="machine in machines" :key="machine.id">
        <div class="card">
          <header class="card-header">
            <p class="card-header-title">{{ machine.hostname }}</p>
          </header>
          <div class="card-content">
            <div class="content">
              <p>IP: {{ machine.ip }}</p>
              <p>Group: {{ machine.groupe }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
    </div>
  </template>
  
  <script>
import NavBar from './NavBar.vue';
import computerService from "@/services/computerService";

  export default {
    components: {
    NavBar,
    },
    data() {
    return {
      machines: [],
    };
  },
  methods: {
    async getMachines() {
      this.machines = await computerService.getAllComputers();
    },
  },
  mounted() {
    this.getMachines();
  },
  };
  </script>
<style>
.banner {
  width: 100%;
}
.card {
  margin-bottom: 1rem;
}
</style>
  