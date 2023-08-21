import { createApp } from 'vue'
import App from './App.vue'
import './index.css'
import router from  "./router"


// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyBQvlyTTsxcBHtgjcTTzBoxA7T5_9Gzwvs",
  authDomain: "loginauthapp-e5759.firebaseapp.com",
  projectId: "loginauthapp-e5759",
  storageBucket: "loginauthapp-e5759.appspot.com",
  messagingSenderId: "7388756833",
  appId: "1:7388756833:web:79bceb8f3384f71de5a320",
  measurementId: "G-VT4CBZ75TV"
};

// Initialize Firebase
initializeApp(firebaseConfig);
const app = createApp(App);


app.use(router)

app.mount('#app')
