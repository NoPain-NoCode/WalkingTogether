import axios from 'axios';


const client = axios.create({
    baseURL: 'http://deeplearner.smu.ac.kr:8000/'
});

export default client;
