<template>
  <section class="hero is-fullheight">
    <div class="hero-body">
      <div class="container">
        <div class="columns is-centered is-vcentered">
          <div class="column is-half">
            <a class="navbar-item" href="/">
              <img src="@/assets/logo-nav.svg" />
            </a>
            <h1>Login</h1>
            <form @submit.prevent="submitForm">
              <div class="field">
                <input class="input" type="text" v-model="username" placeholder="username" required />
              </div>
              <div class="field">
                <input class="input" type="password" v-model="password" placeholder="Password" required />
              </div>
              <div class="field">
                <button class="button is-success">Login</button>
              </div>
            </form>
            <router-link class="navbar-item" to="/">Home</router-link>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import { login } from "@/services/authService";

export default {
  data() {
    return {
      username: "",
      password: "",
    };
  },
  methods: {
    async submitForm() {
      try {
        const response = await login(this.username, this.password);
        localStorage.setItem("access_token", response.access_token);
        this.$router.push("/dashboard");
      } catch (error) {
        console.error(error);
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
