import apiClient from "./index";

export async function login(username, password) {
  try {
    const response = await apiClient.post("/login", {
      username,
      password,
    });

    return response.data;
  } catch (error) {
    console.log(`HTTP error -> ${error.response.status}`);
  }
}

export async function firstTimePassword(username, old_password, new_password, new_password_confirmation) {
  try {
    const response = await apiClient.post("/first-time-password", {
      username,
      old_password,
      new_password,
      new_password_confirmation,
    });

    return response.data;
  } catch (error) {
    console.log(`HTTP error -> ${error.response.status}`);
  }
  
}
// authService.js
export function isAuth() {
  const accessToken = localStorage.getItem("access_token");
  return !!accessToken;
}

export function getAccessToken() {
  return localStorage.getItem("access_token");
}

export function logout() {
  localStorage.removeItem("access_token");
  localStorage.removeItem("user_role");
}
// authService.js
export function isAdmin() {
  const userRole = localStorage.getItem("user_role");
  return userRole === 'admin';
}

