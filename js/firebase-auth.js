// Firebase imports
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.12.2/firebase-app.js";

import {
  getAuth,
  createUserWithEmailAndPassword,
  signInWithEmailAndPassword,
  signOut
} from "https://www.gstatic.com/firebasejs/10.12.2/firebase-auth.js";


const firebaseConfig = {
  apiKey: "AIzaSyDufP0DtgYji2eAOxJJoYMlATuvuqQciK0",
  authDomain: "datamorphai-49a2d.firebaseapp.com",
  projectId: "datamorphai-49a2d",
  storageBucket: "datamorphai-49a2d.firebasestorage.app",
  messagingSenderId: "292675441870",
  appId: "1:292675441870:web:0835350f46428448042c9f",
  measurementId: "G-WDKKTYJL2P"
};


const app = initializeApp(firebaseConfig);
const auth = getAuth(app);


// SIGN UP FUNCTION
window.signUp = function(email, password) {

  createUserWithEmailAndPassword(auth, email, password)

    .then((userCredential) => {

      alert("Account created successfully");

      window.location.href = "dashboard.html";

    })

    .catch((error) => {

      alert(error.message);

    });

};


// SIGN IN FUNCTION
window.signIn = function(email, password) {

  signInWithEmailAndPassword(auth, email, password)

    .then((userCredential) => {

      alert("Login successful");

      window.location.href = "dashboard.html";

    })

    .catch((error) => {

      alert(error.message);

    });

};


// LOGOUT FUNCTION
window.logout = function() {

  signOut(auth).then(() => {

    window.location.href = "index.html";

  });

};