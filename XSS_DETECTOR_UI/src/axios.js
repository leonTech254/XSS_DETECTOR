import axios from 'axios'
// import axios from 'redaxios'
// import axios from 'axios/axios.js';
// import axios from 'redaxios';
// axios.defaults.baseURL='https://api.leonteqsecurity.com/';
// axios.defaults.baseURL='http://192.168.8.200:5000/';
// axios.defaults.baseURL = 'http://192.168.43.226:5000';
// axios.defaults.baseURL='http://192.168.76.225:5000/';
// axios.defaults.baseURL='http://192.168.43.225:5000';
axios.defaults.baseURL='http://127.0.0.1:5000/';
axios.defaults.headers.common['Authorization'] = 'Bearer ' + localStorage.getItem('token')
