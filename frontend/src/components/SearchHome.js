import React , {useState,useEffect} from 'react';
import axios from 'axios';
import Header from './Header';
import MapContainer from './MapContainer';
import MapListItem from './MapListItem';

const SearchHome = ({match})=>{
    const jwtToken = sessionStorage.getItem('jwtToken');

    const searchKeyword = match.params.searchKeyword;
    console.log(match.params.searchKeyword);
    const [results, setResults] = useState([]);

    
    const [markerPositions , setMarkerPositions] = useState([]);
    const [infoNames, setInfoNames] = useState([]);
    const [likedPointList,setLikedPointList] = useState([]);
    const [points, setPoints] = useState([]);

    const mapStyles = {        
        height: "500px",
        width: "500px"};


    const getSearchResult = async ()=>{
       try{
            const searchResult = await axios.post('https://www.wannawalk.co.kr:8001/maps/road_search/',{
                "search":searchKeyword
            })
            console.log(searchResult.data);
            setResults(searchResult.data);

            const markers = searchResult.data.map(res => {
                return {lat:res.latitude, lng:res.longitude};
            });
            // setLikedPointList(response.data.map(res=>{
            //     return res.point_number;
            // }));
            setInfoNames(searchResult.data.map(res=>{
                return res.point_name;
            }));
            setMarkerPositions(markers);
            setPoints(searchResult.data.map(rec=>{
                return rec.point_number;
            }));
        }catch(e){
            console.log(e);
        }
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
                
            }catch(e){
                console.log(e);
            }
        }else{
            setLikedPointList([]);
            console.log(likedPointList);
        }
    }

    useEffect(() => {
        getSearchResult();
        getLikedList();
    },[]);

    return(
        <div className='main-container'>
        <div className='container' style={{margin:"0px"}}>
            <Header />
            <p>"{searchKeyword}" 검색 결과 입니다. </p>
            <div className='map-List'>
                <div className='map-Container'>
                <MapContainer position={markerPositions[0]} markers={markerPositions} mapStyles={mapStyles} names={infoNames} links={points} ></MapContainer>
                </div>
                <div className='list-container'>
                    <div className="list">
                        {results.map(rec => {
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

export default SearchHome;