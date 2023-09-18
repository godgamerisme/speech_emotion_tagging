<template>
    <div class="sign-in-container">
      <h1>Sign In</h1>
      <form @submit.prevent="signin">
        <div class="input-group" style="margin-top: 170px;"> <!-- Add margin-top -->
          <label for="email">Email</label>
          <input
            id="email"
            type="text"
            placeholder="Enter your email"
            v-model="email"
          />
        </div>
        <div class="input-group">
          <label for="password">Password</label>
          <input
            id="password"
            type="password"
            placeholder="Enter your password"
            v-model="password"
          />
        </div>
        <p v-if="errMsg">{{ errMsg }}</p>
        <button type="submit" class="submit-button">Submit</button>
      </form>
      <div class="button-spacing">
        <button @click="google" class="google-button">Sign In With Google</button>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from "vue";
  import { getAuth, signInWithEmailAndPassword } from "firebase/auth";
  import { useRouter } from "vue-router";
  
  const email = ref("");
  const password = ref("");
  const router = useRouter();
  const errMsg = ref();
  
  const signin = () => {
    signInWithEmailAndPassword(getAuth(), email.value, password.value)
      .then((data) => {
        console.log("Successfully signed in!");
        router.push("/videos");
      })
      .catch((error) => {
        console.log(error.code);
        switch (error.code) {
          case "auth/invalid-email":
            errMsg.value = "Invalid email address format.";
            break;
          case "auth/wrong-password":
            errMsg.value = "Incorrect password. Please try again.";
            break;
          case "auth/user-not-found":
            errMsg.value = "User not found. Please register.";
            break;
          default:
            errMsg.value = "Email or Password Incorrect";
            break;
        }
      });
  };
  
  const google = () => {
    // Implement Google Sign-In logic here
  };
  </script>
  
  <style scoped>
  .sign-in-container {
    max-width: 400px;
    margin: 0 auto;
    padding: 20px;
    text-align: center;
  }
  
  h1 {
    font-size: 24px;
    margin-bottom: 20px;
  }
  
  .input-group {
    margin-bottom: 20px;
  }
  
  label {
    display: block;
    margin-bottom: 5px;
    text-align: left;
  }
  
  input {
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
    font-size: 16px;
  }
  
  .submit-button {
    background-color: red;
    color: white;
    border: none;
    border-radius: 5px;
    padding: 10px 20px;
    font-size: 18px;
    cursor: pointer;
  }
  
  .google-button {
    background-color: #4285f4;
    color: white;
    border: none;
    border-radius: 5px;
    padding: 10px 20px;
    font-size: 18px;
    cursor: pointer;
  }
  
  .button-spacing {
    margin-top: 20px; /* Add spacing between buttons */
  }
  </style>
  