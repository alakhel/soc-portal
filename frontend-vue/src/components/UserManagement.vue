<template>
    <NavBar></NavBar>
    <div class="container">
      <div class="column is-narrow"></div>
      <section class="section">
        <div class="columns is-vcentered">
          <div class="column">
            <h1 class="title">User Management</h1>
          </div>
          <div class="column is-narrow"></div>
        </div>
      </section>
      <section class="section">
        <button class="button is-primary" @click="showAddUserModal()">
          Add User
        </button>
        <table class="table is-striped is-hoverable is-fullwidth">
          <thead>
            <tr>
              <th>ID</th>
              <th>First Name</th>
              <th>Last Name</th>
              <th>Username</th>
              <th>Group</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="user in users" :key="user.id">
              <td>{{ user.id }}</td>
              <td>{{ user.prenom }}</td>
              <td>{{ user.nom }}</td>
              <td>{{ user.username }}</td>
              <td>{{ user.groupe }}</td>
              <td>
                <button
                  class="button is-small is-danger"
                  @click="deleteUser(user.id)"
                >
                  Delete
                </button>
                <button
                  class="button is-small is-info"
                  @click="showEditUserModal(user)"
                >
                  Edit
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </section>
    </div>
    <add-edit-user-modal
      v-if="addEditUserModalVisible"
      :edit-mode="editMode"
      :user-data="currentUserData"
      @close="addEditUserModalVisible = false"
      @submit="submitUserForm"
    ></add-edit-user-modal>
</template>
  
<script>
import userService from '@/services/userService';
import NavBar from './NavBar.vue';
import AddEditUserModal from './AddEditUserModal.vue'; // Import the AddEditUserModal component
  
    export default {
      name: "UserManagement",
      data() {
    return {
      users: [],
      addEditUserModalVisible: false,
      editMode: false,
      currentUserData: {},
    };
  },
      methods: {
          async deleteUser(id) {
              try {
                  await userService.deleteUser(id);
                  this.users = this.users.filter(user => user.id !== id);
              }
              catch (error) {
                  console.error("Error deleting user:", error);
              }
          },
          async getUsers() {
              try {
                  const users = await userService.getAllUsers();
                  this.users = users;
              }
              catch (error) {
                  console.error("Error fetching users:", error);
              }
          },
          showAddUserModal() { 
            console.log("showAddUserModal");
        this.editMode = false;
        this.currentUserData = {
          prenom: '',
          nom: '',
          username: '',
          password: '',
          groupe: '',
        };
        this.addEditUserModalVisible = true;
      },
    showEditUserModal(user) {
        console.log("showEditUserModal");

      this.editMode = true;
      this.currentUserData = { ...user };
      this.addEditUserModalVisible = true;
    },
    async submitUserForm(user) {
      if (this.editMode) {
        await userService.updateUser(user.id, user);
      } else {
        await userService.createUser(user);
      }
      this.getUsers();
      this.addEditUserModalVisible = false;
    },
      },
      created() {
          this.getUsers();
      },
      components: { NavBar,AddEditUserModal }
  };
  </script>
  
  <style>
  /* Add any custom styles here */
  </style>
  