import React , {useState, useEffect} from 'react';
import { GoogleMap, InfoWindow, LoadScript, Marker} from '@react-google-maps/api';
import axios from 'axios';

import "../style/removeInfo.css";

const MapContainer = ({position, markers, mapStyles, names,links}) => {
    
    const GOOGLE_MAP_API_KEY = process.env.REACT_APP_GOOGLE_MAP_KEY;
    let cnt=0;


    return (
        <LoadScript
        googleMapsApiKey={GOOGLE_MAP_API_KEY}>
            <GoogleMap
                mapContainerStyle={mapStyles}
                zoom={13}
                center={position}
            >
                <Marker position={position} >
                    
                </Marker>
                
                {markers.map(marker => {
                    // return <Marker key={cnt++} position={marker}></Marker>
                    const keyValue = cnt;
                    return <InfoWindow  key={cnt++} position={marker}><p onClick={()=>{ document.location.href = '/detail/'+links[keyValue]}} style={{fontSize:"5px",cursor:"pointer"}}>{names[cnt]}</p></InfoWindow>
                    }
                )}
            </GoogleMap>
        </LoadScript>
    )
}

MapContainer.defaultProps = {
    position: {lat: 37.5790314, lng: 126.94334850000001},
    markers : [],
    links:[],
    names:[]
};
export default MapContainer;