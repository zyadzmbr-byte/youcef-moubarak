// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-app.js";
import { getFirestore } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-firestore.js";
import { getAuth } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-auth.js";
import { getStorage } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-storage.js";

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyCs7UtckhIxUUi7_VvL0J0HXwZQSyT5zCE",
  authDomain: "yousif-moubarak.firebaseapp.com",
  databaseURL: "https://yousif-moubarak-default-rtdb.firebaseio.com",
  projectId: "yousif-moubarak",
  storageBucket: "yousif-moubarak.firebasestorage.app",
  messagingSenderId: "59895044739",
  appId: "1:59895044739:web:64b1764b913cd9a9e0d9b6"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const db = getFirestore(app);
const auth = getAuth(app);
const storage = getStorage(app);

export { db, auth, storage };
