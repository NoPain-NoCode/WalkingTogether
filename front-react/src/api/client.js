import axios from 'axios';


const client = axios.create({
    baseURL: 'deeplearner.smu.ac.kr'
});

export default client;
