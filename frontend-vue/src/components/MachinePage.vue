<template>
  <div>
    <NavBar></NavBar>
    <section class="section">
      <div class="container">
        <h1 class="title">Machines</h1>
        <table class="table is-striped is-hoverable is-fullwidth">
          <thead>
            <tr>
              <th>Hostname</th>
              <th>IP</th>
              <th>Group</th>
              <th>Action</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="machine in machines" :key="machine.id">
              <td>{{ machine.hostname }}</td>
              <td>{{ machine.ip }}</td>
              <td>{{ machine.groupe }}</td>
              <td>
                <button class="button is-danger" @click="deleteMachine(machine.id)">Delete</button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>
    <section class="section">
      <div class="container">
        <h2 class="title">Add Machine</h2>
        <form @submit.prevent="addMachine">
          <div class="field">
            <label class="label" for="hostname">Hostname</label>
            <div class="control">
              <input class="input" type="text" id="hostname" v-model="newMachine.hostname" required />
            </div>
          </div>

          <div class="field">
            <label class="label" for="ip">IP</label>
            <div class="control">
              <input class="input" type="text" id="ip" v-model="newMachine.ip" required />
            </div>
          </div>

          <div class="field">
            <label class="label" for="groupe">Group</label>
            <div class="control">
              <input class="input" type="text" id="groupe" v-model="newMachine.groupe" required />
            </div>
          </div>

          <div class="field">
            <div class="control">
              <button class="button is-link" type="submit">Add Machine</button>
            </div>
          </div>
        </form>
      </div>
    </section>
  </div>
</template>

<style scoped>
/* Add any custom styles here */
</style>

  <script>
  import NavBar from './NavBar.vue';
  import computerService from '@/services/computerService';
  
  export default {
    name: "MachineList",
    components: {
      NavBar,
    },
    data() {
      return {
        machines: [],
        newMachine: {
          hostname: '',
          ip: '',
          groupe: '',
        },
      };
    },
    methods: {
      async getMachines() {
        this.machines = await computerService.getAllComputers();
      },
      async deleteMachine(id) {
        await computerService.deleteComputer(id);
        this.getMachines();
      },
      async addMachine() {
        await computerService.createComputer(this.newMachine);
        this.getMachines();
        this.newMachine = {
          hostname: '',
          ip: '',
          groupe: '',
        };
      },
    },
    mounted() {
      this.getMachines();
    },
  };
  </script>
  
  