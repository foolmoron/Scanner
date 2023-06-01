const firebaseConfig = {
    apiKey: 'AIzaSyAeg3vlBGHx6q7FZf4t1J1eLOfWpS0o4Zg',
    authDomain: 'scanner-d8c37.firebaseapp.com',
    projectId: 'scanner-d8c37',
    storageBucket: 'scanner-d8c37.appspot.com',
    messagingSenderId: '877826595361',
    appId: '1:877826595361:web:2c3a1498a8e5fd81efe160',
};
firebase.initializeApp(firebaseConfig);
const auth = firebase.auth();
const db = firebase.firestore();
