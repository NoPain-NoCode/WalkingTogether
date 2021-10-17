import React , {useState, useEffect} from 'react';
import { Children } from 'react';
//css 적용
import '../style/walkList_web.css'

import MapContainer from './MapContainer';
import axios from 'axios';

import MapListItem from './MapListItem';
import Header from './Header';


const Home = ()=>{

    const jwtToken = sessionStorage.getItem('jwtToken');

    const [ newCurrentPosition, setNewCurrentPosition ] = useState({lat:'', lng:''});
    const [recomends, setRecomends] = useState([]);
    const [markerPositions , setMarkerPositions] = useState([]);
    const [infoNames, setInfoNames] = useState([]);
    const [likedPointList,setLikedPointList] = useState([]);
    const [points, setPoints] = useState([]);
    
    const mapStyles = {        
        height: "500px",
        width: "500px"};
    

    const postToBack = async (value)=>{
        console.log(value);
        axios.post('https://www.wannawalk.co.kr:8001/maps/near_road/',value)
        .then(response => { 
	        console.log(response.data);
            setRecomends(response.data);
            const markers = response.data.map(res => {
                return {lat:res.latitude, lng:res.longitude};
            });
            //setLikedPointList(response.data.map(res=>{
            //    return res.point_number;
            //}));
            setInfoNames(response.data.map(res=>{
                return res.point_name;
            }));
            setMarkerPositions(markers);
            setPoints(response.data.map(rec=>{
                return rec.point_number;
            }));
            
        })
        .catch(error => {
            console.log(error.response)
        }); 
    }

    const getLikedList = async () =>{
        
        if(jwtToken){
            try{
                const likedRoads = await axios.get('https://www.wannawalk.co.kr:8001/user/liketraillist/',{
                    headers: {
                        'Authorization': `Bearer ${jwtToken}`
                    },
                });
                setLikedPointList(likedRoads.data.map(road => road.walkingtrail.point_number));
                console.log(jwtToken);
            }catch(e){
                console.log(e);
            }
        }else{
            setLikedPointList([]);
            console.log(likedPointList);
        }
    }
    

    useEffect(() => {
        
        const success = position => {
            const currentPosition = {
                lat: position.coords.latitude,
                lng: position.coords.longitude
            }
            setNewCurrentPosition({...newCurrentPosition, lat:currentPosition.lat, lng:currentPosition.lng});
            postToBack(currentPosition);
            getLikedList();
            console.log(currentPosition);
        };
        
        //setNewCurrentPosition({lat: 37.5790314, lng: 126.94334850000001});
        //postToBack(newCurrentPosition);
        //postToBack({lat: 37.5790314, lng: 126.94334850000001});
        
        
        navigator.geolocation.getCurrentPosition(success);
        getLikedList();
    
        //postToBack(newCurrentPosition);
    },[]);
    //<MapContainer position={newCurrentPosition} markers={markerPositions} mapStyles={mapStyles} names={infoNames} ></MapContainer>
    
    return(
        <div className='main-container'>
            <div className='container' style={{margin:"0px"}}>
                <Header />
                <div className='map-List'>
                    <div className='map-Container'>
                    <MapContainer position={newCurrentPosition} markers={markerPositions} mapStyles={mapStyles} names={infoNames} links={points} ></MapContainer>
                    </div>
                    <div className='list-container'>
                        <div className="list">
                            {recomends.length === 0 ?<div>현재 서울 지역만 서비스 하고 있습니다.죄송합니다.</div> : recomends.map(rec => {
                                                    return  likedPointList.includes(rec.point_number) ?  
                                                        <MapListItem className="box" recommend={rec} jwtToken={jwtToken} liked={true}></MapListItem>
                                                        :
                                                        <MapListItem className="box" recommend={rec} jwtToken={jwtToken} liked={false}></MapListItem>
                                                })}
                        </div>  
                    </div>
                </div>
                
            </div>
            
            
            
        </div>
        
            
    );
    
}

export default Home;