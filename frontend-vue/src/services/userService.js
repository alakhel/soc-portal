import apiClient from './index';

export default {
  async getAllUsers() {
    const response = await apiClient.get('/users');
    return response.data;
  },

  async createUser(data) {
    const response = await apiClient.post('/users', data);
    return response.data;
  },

  async updateUser(id, data) {
    const response = await apiClient.put(`/users/${id}`, data);
    return response.data;
  },

  async getUserById(id) {
    const response = await apiClient.get(`/users/${id}`);
    return response.data;
  },

  async deleteUser(id) {
    const response = await apiClient.delete(`/users/${id}`);
    return response.status;
  },
  async getAuthenticatedUser() {
    const response = await apiClient.get('/user');
    return response.data;
  },
};
