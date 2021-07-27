import axios from 'axios';


const API = axios.create();


const getRecommendURL = 'http://localhost:8000/api/near_walk'


export const getRecommendList = () => API.get(getRecommendURL); 
export const postUserLocation = ((response) => API.post(getRecommendURL, response));