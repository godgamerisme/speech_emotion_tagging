<template>
  <section class="vh-100">
    <div class="container py-5 h-100">
      <div class="row d-flex justify-content-center align-items-center h-100">
        <div class="col-12 col-md-8 col-lg-6 col-xl-5">
          <div class="card shadow-2-strong" style="border-radius: 1rem">
            <div class="card-body p-5 text-center">
              <div class="d-flex gap-2 justify-content-center">
                <img
                  src="@/assets/heartballoon.png"
                  alt="HeartBalloon"
                  class="heartballoon"
                />
                <h2 class="mb-5">MindScape</h2>
              </div>

              <div class="form-outline mb-4">
                <input
                  type="email"
                  id="typeEmailX-2"
                  class="form-control form-control-lg"
                  placeholder="Enter your email"
                  v-model="email"
                />
                <label class="form-label" for="typeEmailX-2">Email</label>
              </div>

              <div class="form-outline mb-4">
                <input
                  type="password"
                  id="typePasswordX-2"
                  class="form-control form-control-lg"
                  placeholder="Enter your password"
                  v-model="password"
                />
                <label class="form-label" for="typePasswordX-2">Password</label>
              </div>

              <div class="d-grid gap-2">
                <button
                  class="btn btn-primary btn-lg btn-block"
                  type="submit"
                  @click="signin"
                >
                  Log in
                </button>
                <hr class="my-4" />

                <button
                  class="btn btn-lg btn-block btn-secondary"
                  type="submit"
                  @click="google"
                >
                  <i class="bi bi-google"></i> Sign in with google
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref } from "vue";
import {
  getAuth,
  signInWithEmailAndPassword,
  GoogleAuthProvider,
  signInWithPopup,
} from "firebase/auth";
import { useRouter } from "vue-router";

const email = ref("");
const password = ref("");
const router = useRouter();
const errMsg = ref();

const signin = () => {
  const auth = getAuth();
  signInWithEmailAndPassword(auth, email.value, password.value)
    .then((data) => {
      console.log("Successfully signed in!");
      console.log(auth.currentUser);
      router.push("/home");
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
  const provider = new GoogleAuthProvider();
  signInWithPopup(getAuth(), provider)
    .then((result) => {
      console.log(result.user);
      router.push("/home");
    })
    .catch((error) => {
      console.log(error.code);
      alert(error.message);
    });
};
</script>

<style scoped>
.heartballoon {
  width: 50px;
  height: 50%;
}
</style>
