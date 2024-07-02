import { initializeApp } from "https://www.gstatic.com/firebasejs/10.12.2/firebase-app.js";
import { getAnalytics } from "https://www.gstatic.com/firebasejs/10.12.2/firebase-analytics.js";
const firebaseConfig = {
  apiKey: "AIzaSyDrjPqkG1CSpVU_CLDBY3Mo7cgbOdxvT6w",
  authDomain: "kumo-at.firebaseapp.com",
  projectId: "kumo-at",
  storageBucket: "kumo-at.appspot.com",
  messagingSenderId: "172841332677",
  appId: "1:172841332677:web:f63ab60f476cb5004ba5ac",
  measurementId: "G-WW09DE7HQT"
};
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);

const loginForm = document.getElementById('loginForm');

loginForm.addEventListener('submit', function(event) {
    event.preventDefault();
    const email = loginForm.email.value;
    const password = loginForm.password.value;

    signInWithEmailAndPassword(auth, email, password)
        .then((userCredential) => {

            const user = userCredential.user;
            console.log('User logged in:', user);
            window.location.href = '/logged';
        })
        .catch((error) => {

            const errorCode = error.code;
            const errorMessage = error.message;
            console.error('Login error:', errorMessage);
        });
});