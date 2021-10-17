import React from 'react';
import MapContainer from './MapContainer';
import MapListContainer from './MapListContainer';


const MapTemplate = ({children})=>{
    return (
        <div className='MapTemplate'>
            <div className='content'>{children}</div>
        </div>
        
    );
}

export default MapTemplate;