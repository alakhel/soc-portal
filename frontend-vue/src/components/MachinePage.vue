<template>
    <div>
        <NavBar></NavBar>
      <section class="section">
        <div class="container">
          <!-- The Machine List content -->
          <h1>MACHINE</h1>
        </div>
      </section>
      <section class="section">
        <div class="container">
          <!-- The Add Machine form content -->
        </div>
      </section>
    </div>
  </template>
  
  <script>
  import NavBar from './NavBar.vue';

  export default {
    name: "MachineList",
    components: {
        NavBar,
      },
    data() {
      return {
        machines: []
      };
    },
    methods: {
      getMachines() {
        // Fetch the machine data from the API
      },
      deleteMachine(id) {
        // Delete the machine with the given ID
        return id;
      },
      addMachine() {
        // Add a new machine
      }
    },
    mounted() {
      this.getMachines();
    }
  };
  </script>
  
  <style scoped>
  /* Add any custom styles here */
  </style>
  