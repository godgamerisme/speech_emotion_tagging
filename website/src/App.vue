<template>
  <nav>
    <router-link to="/"> Home</router-link> |
    <router-link to="/register"> Register</router-link> |
    <router-link to="/sign-in"> Sign In</router-link> |
    <router-link to="/videos"> All Videos</router-link> | 
    <router-link to="/video-player"> Video Player</router-link> | 
    <router-link to="/upload"> Upload Page</router-link> | 
    <button class ="btn" @click="handleSignOut" v-if="isLoggedIn"> Sign Out</button>
  </nav>
  <router-view />
</template>

<script setup>
import { onMounted, ref } from 'vue';
import { getAuth, onAuthStateChanged, signOut } from "firebase/auth"
import router from './router';

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

nav {
  font-size: 25px; /* Adjust the font size as needed */
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
