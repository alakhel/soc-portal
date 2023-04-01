<template>
    <div class="profile-page">
      <NavBar></NavBar>
      <section class="section">
        <div class="container">
          <h1 class="title">User Profile</h1>
          <div class="box" v-if="user">
            <div class="content">
              <p>ID: {{ user.id }}</p>
              <p>First Name: {{ user.prenom }}</p>
              <p>Last Name: {{ user.nom }}</p>
              <p>Username: {{ user.username }}</p>
              <p>First Login: {{ user.firstLogin ? 'Yes' : 'No' }}</p>
              <p>Group: {{ user.groupe }}</p>
              <p>Created At: {{ user.created_at }}</p>
              <p>Updated At: {{ user.updated_at }}</p>
            </div>
            <div class="has-text-right">
              <button class="button is-primary" @click="showEditUserModal(user)">Edit</button>
            </div>
          </div>
          <div v-else>
            <p>Loading user information...</p>
          </div>
        </div>
      </section>
      <add-edit-user-modal
        v-if="addEditUserModalVisible"
        :edit-mode="editMode"
        :user-data="currentUserData"
        @close="addEditUserModalVisible = false"
        @submit="submitUserForm"
      ></add-edit-user-modal>
    </div>
  </template>
<script>
import NavBar from './NavBar.vue';
import userService from '@/services/userService';
import AddEditUserModal from './AddEditUserModal.vue'; // Import the AddEditUserModal component

export default {
  name: 'ProfilePage',
  components: {
    NavBar,
    AddEditUserModal,
  },
  data() {
    return {
      user: null,
      addEditUserModalVisible: false,
      editMode: true,
      currentUserData: {},
    };
  },
  methods: {
    showEditUserModal(user) {
      this.editMode = true;
      this.currentUserData = { ...user };
      this.addEditUserModalVisible = true;
    },
    async submitUserForm(user) {
      await userService.updateUser(user.id, user);
      this.user = { ...user };
      this.addEditUserModalVisible = false;
    },
  },
  async created() {
    try {
      const authenticatedUser = await userService.getAuthenticatedUser();
      this.user = authenticatedUser;
    } catch (error) {
      console.error('Error fetching authenticated user:', error);
    }
  },
};
</script>
  