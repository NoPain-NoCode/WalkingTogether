import React , {useState,useEffect} from 'react';

import axios from 'axios';
import {Link} from 'react-router-dom';
import {
    MdFavorite,
    MdFavoriteBorder,
    MdSettingsInputAntenna
} from 'react-icons/md';


const MapListItem = ({recommend,jwtToken,liked})=>{ 

    const {Transportation,category,course_detail,course_name,distance,latitude,longitude,point_name,point_number,region,subway,time_required,_explain,_level} = recommend;
    const moveLink = '/detail/'+point_number;
    const posturl = 'https://www.wannawalk.co.kr:8001/user/clickliketrail/'+point_number+'/';
    
    const [likedState , setLiked] = useState(liked);

    useEffect(() => {
        setLiked(liked);
    },[liked])

    const onHeartClick = async()=>{
        if(!jwtToken){
            alert('로그인 해야 사용할 수 있는 기능입니다. 로그인 해 주세요');
            document.location.href = '/login';
        }
        else{
            try{
                if (likedState){
                    setLiked(false);
                    const likeDeleteRequest = await axios.delete(posturl,{headers: {
                        'Authorization': `Bearer ${jwtToken}`
                    }},)
                    console.log(likeDeleteRequest);
                }
                else {
                    setLiked(true);
                    const likePostRequest = await axios.post(posturl,{},{headers: {
                        'Authorization': `Bearer ${jwtToken}`
                    }},)
                    console.log(likePostRequest);
                }
            }catch(e){
                console.log(e);
            }
        }
    }
    
    return (
        
        <div className="box" style={{marginLeft:"5px"}}>
            
            <div className="info">
                <Link to={moveLink} style={{ color: 'inherit',textDecoration: 'none' }} >
                    <div className="path_name">포인트명:{point_name}</div>
                    <div className="path_address">코스명:{course_name}</div>
                </Link>
            </div>
            
                
            <div className="heart">
                {!likedState ? <MdFavoriteBorder className='heart-img' onClick={onHeartClick}/>:<MdFavorite className='heart-img' onClick={onHeartClick}/>}
            </div>
        </div>
        
        
    );

}

export default MapListItem;