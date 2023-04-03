<template>
    <section class="hero is-fullheight">
      <div class="hero-body">
        <div class="container">
          <div class="columns is-centered is-vcentered">
            <div class="column is-half">
              <h1>Login</h1>
              <form @submit.prevent="submitForm">
                <div class="field">
                  <p class="control has-icons-left has-icons-right">
                    <input class="input" type="text" v-model="username" placeholder="username" required>
                    <span class="icon is-small is-left">
                      <i class="fas fa-envelope"></i>
                    </span>
                    <span class="icon is-small is-right">
                      <i class="fas fa-check"></i>
                    </span>
                  </p>
                </div>
                <div class="field">
                  <p class="control has-icons-left">
                    <input class="input" type="password" v-model="password" placeholder="Password" required>
                    <span class="icon is-small is-left">
                      <i class="fas fa-lock"></i>
                    </span>
                  </p>
                </div>
                <div class="field">
                  <p class="control">
                    <button class="button is-success">
                      Login
                    </button>
                  </p>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
    </section>
  </template>
  
  <script>
  export default {
    data() {
      return {
        username: "",
        password: "",
      };
    },
    methods: {
      submitForm() {
        const data = {
          username: this.username,
          password: this.password,
        };
        fetch('/login', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(data)
        }).then(response => response.json()).then(data => {
          console.log(data)
          localStorage.setItem('access_token', data.access_token);
          this.$router.push('/dashboard');
        }).catch(error => console.error(error));
      },
    },
  };
  </script>
  
  <style>
  input[type="text"], input[type="password"] {
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
  
  .icon.is-small.is-left, .icon.is-small.is-right {
    margin-top: 10px;
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
  