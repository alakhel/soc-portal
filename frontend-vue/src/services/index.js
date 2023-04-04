import axios from 'axios';

const apiClient = axios.create({
 // baseURL: 'http://127.0.0.1:8000/api',
  baseURL: 'http://64.226.68.181/api',
  // Configure your axios instance here
});

apiClient.interceptors.request.use((config) => {
  const token = localStorage.getItem('access_token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
}, (error) => {
  return Promise.reject(error);
});

apiClient.interceptors.response.use((response) => {
  return response;
}, (error) => {
  if (error.response && error.response.status === 422) {
    // Handle 422 Unprocessable Entity error here
    console.error('Validation errors:', error.response.data.errors);
  }
  return Promise.reject(error);
});

export default apiClient;
