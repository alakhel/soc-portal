<template>
    <div class="modal is-active">
      <div class="modal-background" @click="$emit('close')"></div>
      <div class="modal-card">
        <header class="modal-card-head">
          <p class="modal-card-title">{{ editMode ? 'Edit User' : 'Add User' }}</p>
        <button class="delete" aria-label="close" @click="$emit('close')"></button>
      </header>
      <section class="modal-card-body">
        <add-edit-user
          :submit-label="editMode ? 'Update User' : 'Create User'"
          :user-data="userData"
          @submit="submitForm"
        ></add-edit-user>
      </section>
    </div>
  </div>
</template>
<script>
import AddEditUser from './AddEditUser.vue';

export default {
  components: {
    AddEditUser,
  },
  props: {
    editMode: Boolean,
    userData: Object,
  },
  methods: {
    submitForm(user) {
      this.$emit('submit', user);
    },
  },
};
</script>
<style scoped>
.modal-card {
  max-width: 500px;
}
</style>  