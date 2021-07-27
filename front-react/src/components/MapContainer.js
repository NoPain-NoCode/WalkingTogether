import React,{useState,useEffect} from 'react';
import {GoogleMap, LoadScript} from '@react-google-maps/api';
import {getRecommendList, postUserLocation} from '../api/api'
import axios from 'axios';

const MapContainer = ()=>{
    const [ currentPosition, setCurrentPosition ] = useState({});
    const success = position =>{
        const currentPosition = {
            lat: position.coords.latitude,
            lng: position.coords.longitude
        }
        setCurrentPosition(currentPosition);
    };
    //백에게 post로 currentPosition 보냄. 
    const postToBack = async ()=>{
        try{
            const usersLocation = await postUserLocation(currentPosition)
        } catch(error){
            console.error(error);
        }
    }

    useEffect(() => {
        navigator.geolocation.getCurrentPosition(success);
    })

    const mapStyles = {
        height:'500px',
        width:'500px'
    }; 

    return (
        <LoadScript googleMapsApiKey='AIzaSyC-nA3O10Yi5SD7bRZOQjpGKP7GFTgATiA'>
            <GoogleMap 
                mapContainerStyle={mapStyles}
                zoom={13}
                center = {currentPosition}
                onClick={postToBack}
            />
        </LoadScript>
    )
}

export default MapContainer;