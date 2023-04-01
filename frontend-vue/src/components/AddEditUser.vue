<template>
    <div>
      <div class="field">
        <label class="label">First Name</label>
        <div class="control">
          <input class="input" type="text" v-model="user.prenom" required>
        </div>
      </div>
  
      <div class="field">
        <label class="label">Last Name</label>
        <div class="control">
          <input class="input" type="text" v-model="user.nom" required>
        </div>
      </div>
  
      <div class="field">
        <label class="label">Username</label>
        <div class="control">
          <input class="input" type="text" v-model="user.username" required>
        </div>
      </div>
  
      <div class="field">
        <label class="label">Password</label>
        <div class="control">
          <input class="input" type="password" v-model="user.password" required>
        </div>
      </div>
  
      <div class="field">
        <label class="label">Group</label>
        <div class="control">
          <input class="input" type="text" v-model="user.groupe" required>
        </div>
      </div>
  
      <button class="button is-primary" @click="submitForm">{{ submitLabel }}</button>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      submitLabel: String,
      userData: Object,
    },
    data() {
      return {
        user: { ...this.userData },
      };
    },
    methods: {
      submitForm() {
        this.$emit("submit", this.user);
      },
    },
  };
  </script>
  