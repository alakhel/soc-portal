import apiClient from './index';

export async function login(username, password) {
  try {
    const response = await apiClient.post('/login', {
      username,
      password,
    });

    return response.data;
  } catch (error) {
    throw new Error(`HTTP error ${error.response.status}`);
  }
}
