<template>
  <Navbar @onSignOut="handleSignOut" :isLoggedIn="isLoggedIn" />
  <router-view />
</template>

<script setup>
import { onMounted, ref } from "vue";
import { getAuth, onAuthStateChanged, signOut } from "firebase/auth";
import router from "./router";
import Navbar from "./components/Navbar.vue";

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
    isLoggedIn.value = false;
    router.push("/");
  });
};
</script>
