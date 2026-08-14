import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";
import { getFirestore } from "firebase/firestore";
import { getStorage } from "firebase/storage";

const firebaseConfig = {
  apiKey: "AIzaSyCsd7oFSWNE4XX64DKw_tu2hdmxQ4VUV_M",
  authDomain: "fixpro-7b397.firebaseapp.com",
  projectId: "fixpro-7b397",
  storageBucket: "fixpro-7b397.firebasestorage.app",
  messagingSenderId: "47255768794",
  appId: "1:47255768794:web:9730468e61489650545fe3"
};

const app = initializeApp(firebaseConfig);
export const auth = getAuth(app);
export const db = getFirestore(app);
export const storage = getStorage(app);