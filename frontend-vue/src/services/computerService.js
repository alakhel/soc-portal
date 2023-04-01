import apiClient from './index';

export default {
  async getAllComputers() {
    const response = await apiClient.get('/computers');
    return response.data;
  },

  async createComputer(computerData) {
    const response = await apiClient.post('/computers', computerData);
    console.log(response.data);
    return response.data;
  },

  async getComputerById(id) {
    const response = await apiClient.get(`/computers/${id}`);
    return response.data;
  },

  async updateComputer(id, computerData) {
    const response = await apiClient.put(`/computers/${id}`, computerData);
    return response.data;
  },

  async deleteComputer(id) {
    const response = await apiClient.delete(`/computers/${id}`);
    return response.data;
  },
};
