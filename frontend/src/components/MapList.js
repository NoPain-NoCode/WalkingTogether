import React, {useState, useEffect} from 'react';
import client from '../api/client'

const MapList=()=>{
    const [recommend, setRecommend] = useState(null);
    const [loading, setLoading] = useState(false);
    
    useEffect(()=>{
        const getMapList = async ()=>{
            try{
                const response = await client.get('api/near_walk');
                console.log(response.data);
            }catch(error){
                console.error(error);
            }
        }
        getMapList();
    },[]);

    
    return (
        <div>잘 보이나요?</div>
    );

    
}

export default MapList;