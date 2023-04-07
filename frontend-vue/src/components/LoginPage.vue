<template>
  <section class="hero is-fullheight">
    <div class="hero-body">
      <div class="container">
        <div class="columns is-centered is-vcentered">
          <div class="column is-half">
            <a class="navbar-item" href="/">
              <img src="@/assets/logo-nav.svg" />
            </a>
            <h1 class="title">-Login-</h1>
            <form v-if="!firstTimeLogin" @submit.prevent="submitForm">
              <div class="field">
                <input class="input" type="text" v-model="username" placeholder="Username" required />
              </div>
              <div class="field">
                <input class="input" type="password" v-model="password" placeholder="Password" required />
              </div>
              <div class="field">
                <button class="button is-success">Login</button>
              </div>
            </form>
            <form v-else @submit.prevent="submitFirstTimePassword">
              <h2 class="subtitle">Please change your password</h2>
              <div class="field">
                <input class="input" type="password" v-model="newPassword" placeholder="New Password" required />
              </div>
              <div class="field">
                <input class="input" type="password" v-model="newPasswordConfirmation" placeholder="Confirm New Password" required />
              </div>
              <div class="field">
                <button class="button is-success">Update Password</button>
              </div>
            </form>
            <p v-if="errorMessage" class="has-text-danger">{{ errorMessage }}</p>

            <router-link class="navbar-item" to="/">Home</router-link>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import { login, firstTimePassword } from "@/services/authService";

export default {
  data() {
    return {
      username: "",
      password: "",
      newPassword: "",
      newPasswordConfirmation: "",
      firstTimeLogin: false,
      errorMessage: "",

    };
  },
  methods: {
    async submitForm() {
  try {
    const response = await login(this.username, this.password);
    if (response.message) {
      this.firstTimeLogin = true;
    } else {
      localStorage.setItem("access_token", response.access_token);
      this.$router.push("/dashboard");
    }
  } catch (error) {
    console.log("Error: ", error);
    this.errorMessage = "Invalid username or password";
  }
},
async submitFirstTimePassword() {
  try {
    const response = await firstTimePassword(
      this.username,
      this.password,
      this.newPassword,
      this.newPasswordConfirmation
    );
    // Store the access token and navigate to the dashboard
    localStorage.setItem("access_token", response.access_token);
    this.$router.push("/dashboard");
  } catch (error) {
    console.log("Error: ", error);
  }
},

  },
};
</script>

<style>
input[type="text"],
input[type="password"] {
  border-radius: 5px;
  padding: 10px;
  margin-bottom: 10px;
  width: 100%;
}

button {
  background-color: #3c3c3c;
  border: none;
  border-radius: 5px;
  color: #fff;
  cursor: pointer;
  font-size: 18px;
  font-weight: bold;
  margin-top: 10px;
  padding: 10px;
  width: 100%;
}

button:hover {
  background-color: #555;
}

.hero.is-fullheight {
  display: flex;
}

.hero-body {
  align-items: center;
  justify-content: center;
}

.container {
  max-width: 960px;
}
</style>
