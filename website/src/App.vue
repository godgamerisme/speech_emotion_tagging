<template>
  <Navbar @onSignOut="handleSignOut" :isLoggedIn="isLoggedIn" />
  <router-view />
</template>

<script setup>
import { onMounted, ref } from 'vue';
import { getAuth, onAuthStateChanged, signOut } from "firebase/auth"
import router from './router';
import Navbar from './components/Navbar.vue';

const isLoggedIn = ref(false);

let auth;
onMounted(() => {
  auth = getAuth();
  onAuthStateChanged(auth, (user) => {
    if (user) {
      isLoggedIn.value = true;
    } else {
      isLoggedIn.value = false;
    }
  });
});

const handleSignOut = () => {
  signOut(auth).then(() => {
    router.push("/")
  });
};

</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

router-link {
  text-decoration: none; /* Remove underline from router-links */
  color: #333; /* Change the color as needed */
  margin: 0 10px; /* Add margin to separate the links */
}

.btn {
  background-color: red;
  color: #fff;
  padding: 5px 10px; /* Adjust padding to make it smaller */
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.btn:hover {
  background-color: darkred;
}

</style>
