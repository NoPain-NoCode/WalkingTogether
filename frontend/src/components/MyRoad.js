import axios from 'axios';
import React, {useState, useEffect} from 'react';
import Header from './Header';
import Navigator from './Navigator';
import MapListItem from './MapListItem';


const MyRoad = ()=>{
    let cnt = 0;
    const contaiberStyle = {
        width:"fit-content",
	    height: "500px",
	    overFlow: "scroll",
	    borderRadius: "15px",
	    marginLeft: "15px",
        marginTop:"10px"
    }
    const likedStyle = {
        display: "grid",
        gridTemplateColumns: "repeat(2, 1fr)",
        
      }

    const [recomends, setRecomends] = useState([{'':''}]);

    const jwtToken = sessionStorage.getItem('jwtToken');

    const getLikedRoad = async()=>{
        try{
            const likedRoads = await axios.get('https://www.wannawalk.co.kr:8001/user/liketraillist/',{
                headers: {
                    'Authorization': `Bearer ${jwtToken}`
                },
            });
            
            console.log(likedRoads);
            console.log(likedRoads.data[0].walkingtrail);
            const lists = likedRoads.data.map(road => road.walkingtrail);
            console.log(lists);
            setRecomends(lists);
            console.log(recomends);
        }catch(e){
            console.log(e);
        }    
    }
    
    useEffect(() => {
        getLikedRoad();
    }, []);

    return (
        <div className="main-container">
            <div className="container">
                <Header />
                <div className='container2'>
                    <Navigator />
                <div style={contaiberStyle}>
                    <div  style={likedStyle}>
                        {recomends.length != 0 ?recomends.map(rec => <MapListItem key={cnt++} recommend={rec} jwtToken={jwtToken} liked={true}></MapListItem>):<div>아직 찜한 산책로가 없어요! 마음에 드는 산책로를 찜 해주세요</div>}
                    </div>
                </div>    
                
                
                </div>
            </div>
        </div>
    );
    


}

export default MyRoad;