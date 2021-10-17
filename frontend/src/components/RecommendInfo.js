import React, {useState, useEffect} from 'react';
import axios from 'axios';
import { GoogleMap, LoadScript, Marker} from '@react-google-maps/api';

import Header from './Header';
import RoadReview from './RoadReview';

import '../style/courseDetail.css';
import MapContainer from './MapContainer';
import ReviewListItem from './ReviewListItem';
import GlobalStyles from './GlobalStyles';

const RecommendInfo = ({match})=>{
    // const [infoDetail, setInfoDetail] = ({});
    const [detailInfo, setDetailInfo] = useState({point_name:'',course_name:'',course_detail:'',region:'',time_required:'',Transportation:'',category:'',_explain:'',point_list:[]});
    const {pointNum} = match.params;
    const [transport, setTransport] = useState([]);
    
    const [reviews, setReviews] = useState([]);
    const [newPoints, setNewPoints] = useState();
 
    const geturl = 'https://www.wannawalk.co.kr:8001/maps/road_detail/'+pointNum+'/';
    
    const getReviewUrl = 'https://www.wannawalk.co.kr:8001/maps/review/list/'+pointNum+'/';
    const jwtToken = sessionStorage.getItem('jwtToken');

    const getRoadDetail = async()=>{
        try{
            const roadDetail = await axios.get(geturl);

            setDetailInfo(
                {   ...detailInfo, 
                    point_name:roadDetail.data.point_name,
                    course_name:roadDetail.data.course_name,
                    course_detail:roadDetail.data.course_detail,
                    region:roadDetail.data.region,
                    time_required:roadDetail.data.region,
                    Transportation:roadDetail.data.Transportation.split('<br />').map(val => <div>{val}</div>),
                    point_list: roadDetail.data.point_list.map(point=>{
                            return {lat:point[1], lng:point[0]};
                            }) ,
                    point_names:  roadDetail.data.point_list.map(point=>point[2]),
                    point_number_list:  roadDetail.data.point_list.map(point=>point[3]),
                    distance:roadDetail.data.distance,
                    subway:roadDetail.data.subway,
                    category:roadDetail.data.category,
                    _explain:roadDetail.data._explain,
                    point_mean: roadDetail.data.point_mean,
                    ok:Number(roadDetail.data.dog_mean.ok),
                    no:Number(roadDetail.data.dog_mean.no),
                    dontknow:Number(roadDetail.data.dog_mean.dontknow),
                });
            console.log(roadDetail.data);
            
            
        
        }catch(e){
            console.log(e);
        }
    }

    const getRoadReview = async ()=>{
        try{
            const roadReview = await axios.get(getReviewUrl);
            console.log(roadReview.data);
            const roadReviews = roadReview.data.map(res => {
                return {content:res.content, point:parseInt(res.point), dogPossible:res.dog_possible, date:res.updated_date.slice(0,10)};
            });
            setReviews(roadReviews);
            console.log(reviews);
        }catch(e){
            console.log(e);
        }
    }


    const mapStyles = {        
        height: "400px",
        width: "800px"};
    
    useEffect(() => {
        getRoadReview();
        getRoadDetail();
    }, []);
        

    const [modalOn, setModalOn] = React.useState(false); 

    const onOpenModal = () => {
        setModalOn(!modalOn);
    }

    const Modal = () => {
        return (
         <div className="modal"> 
            <div className="bg"></div>
             <div className="modalBox"> 
                <button className="closeBtn" onClick={onOpenModal}>✖</button> 
                <RoadReview  pointNum={pointNum} />
                
            </div> 
        </div>
        );
    };
    
    return(
        <div className="main-container">
            
            <Header />
            <div className="main-container">
            <div className="info-container">
                <div className="course-title">{detailInfo.point_name}</div>
                <div className="road-info">
                    <div className="info-title course-name">주소</div>
                    <div className="info-content course-name">{detailInfo.course_name}</div>
                    
                    <div className="info-title course-name">지역</div>
                    <div className="info-content">{detailInfo.region}</div>

                    <div className="info-title course-name">거리</div>
                    <div className="info-content">{detailInfo.distance}</div>

                    <div className="info-title course-name">지하철</div>
                    <div className="info-content">{detailInfo.subway}</div>

                    <div className="info-title course-name">교통</div>
                    <div className="info-content">{detailInfo.Transportation}</div>

                    <div className="info-title course-name">코스 상세</div>
                    <div className="info-content">{detailInfo.course_detail}</div>
                    
                    <div className="info-title course-name">코스 설명</div>
                    <div className="info-content" dangerouslySetInnerHTML={ {__html: detailInfo._explain} }></div>
                </div>
                
                <div className="map-List">
                    <MapContainer position={detailInfo.point_list[0]} markers={detailInfo.point_list} mapStyles={mapStyles} names={detailInfo.point_names} links={detailInfo.point_number_list}/>
                </div>

                <div className="review-container">
                    <div className="review-count">리뷰 ({reviews.length} 개){"★".repeat(detailInfo.point_mean)}{reviews.length>0 ?<div style={{fontSize:"17px"}}> 🦮 반려동물 동반 가능 여부: 가능({detailInfo.ok*100}%) 불가능 ({detailInfo.no*100}%) 모르겠어요({detailInfo.dontknow*100}%) </div>:''}</div>  
                    <div className="review-box">
                        <div className="review-btn"><button class="review-btn" onClick={onOpenModal}>리뷰 쓰기</button></div>
                    </div>
                    {modalOn? <Modal/>: ''}
                </div>
                <div className="comment-list">
                    {reviews.length === 0 ? <div className="review-null">아직 리뷰가 없어요.<br />이용 후 리뷰를 작성 해주세요!</div>: reviews.map(review => <ReviewListItem content={review.content} point={review.point} dogPossible={review.dogPossible} date={review.date} />)}
                    
                </div>
            </div>
        </div>
        
            
            <div></div>
            
            
            

        </div>
    );
}

export default RecommendInfo;