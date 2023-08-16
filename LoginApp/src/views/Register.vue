<template>
    <h1>Create an Account</h1>
    <p><input type="text" placeholder="Email" v-model="email"></p>  <!-- v-model to link data to vars in script -->
    <p><input type="password" placeholder="Password" v-model="password"></p>
    <p><button @click="register">Register</button></p>
    <p><button @click="signInWithGoogle">Sign In With Google</button></p>
</template>

<script setup>
import {ref} from "vue";
import {
    getAuth, 
    createUserWithEmailAndPassword,
    GoogleAuthProvider,
    signInWithPopup,
} from "firebase/auth"
import {useRouter} from 'vue-router'
const email = ref ("")
const password = ref("")
const router = useRouter()

const register = () => {
    createUserWithEmailAndPassword(getAuth(), email.value, password.value)
    .then((data) => {
        console.log("Successfully registered!")
        router.push('/allVideos')
    }).catch((error) => {
        console.log(error.code);
        alert(error.message);
    })
};

const signInWithGoogle = () => {
    const provider = new GoogleAuthProvider();
    signInWithPopup(getAuth(), provider)
    .then((result) => {
        console.log(result.user);
        router.push("/allVideos")
    })
    .catch((error) => {

    });
};

</script>