<template>
    <h1>Sign In</h1>
    <p><input type="text" placeholder="Email" v-model="email"></p>  <!-- v-model to link data to vars in script -->
    <p><input type="password" placeholder="Password" v-model="password"></p>
    <p v-if="errMsg">{{ errMsg }}</p>
    <p><button @click="signIn">Sign In</button></p>
    <p><button @click="signInWithGoogle">Sign In With Google</button></p>
</template>

<script setup>
import {ref} from "vue";
import {getAuth, signInWithEmailAndPassword} from "firebase/auth"
import {useRouter} from 'vue-router'
const email = ref ("")
const password = ref("")
const errMsg = ref()
const router = useRouter()

const signIn = () => {
    signInWithEmailAndPassword(getAuth(), email.value, password.value)
    .then((data) => {
        console.log("Successfully registered!")
        router.push('/allVideos')
    }).catch((error) => {
        console.log(error.code);
        switch (error.code) {
            case "auth/invalid-email":
                errMsg.value = "Invalid email";
                break;
            case "auth/user-not-found":
                errMsg.value = "No user with that email";
                break;
            case "auth/wrong-password":
                errMsg.value = "Incorrect password";
                break;
            default:
                errMsg.value = "Email or password was incorrect";
                break;
        }
    })
};

const signInWithGoogle = () => {

};

</script>