import React , {useState,useEffect}from 'react';


import axios from 'axios';
import Header from './Header'
import Navigator from './Navigator';
import "../style/myComment.css";

import styled from 'styled-components';
import GlobalStyles from './GlobalStyles';
import RoadReview from './RoadReview';

const ReviewBox = styled.div`
    padding: 20px;
    background-color: var(--main-bg-color);
    border-radius: 15px;
    margin-bottom: 10px;
`;

const ReviewComponent = ({info})=>{
    const jwtToken = sessionStorage.getItem("jwtToken");
    const updateUrl = 'https://www.wannawalk.co.kr:8001/maps/review/update/'+info.id+'/';
    
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
                <RoadReview  pointNum={info.walkingtrails} infos={info}/>
                
            </div> 
        </div>
        );
    };


    const onDeleteClick = async ()=>{
        try{
            const deleteReview = await axios.delete(updateUrl,{
                headers: {
                    'Authorization': `Bearer ${jwtToken}`
                },
            })
            alert('리뷰 삭제 완료');
            console.log(deleteReview);
            document.location.href = "/myReview";
        }catch(e){
            console.log(e);
        } 
    }

    return(
        <ReviewBox>
                            <div className="infoBox">
                                <div className="point">{"★".repeat(info.point)}</div>
                                <div className="pointName">
                                    포인트명: {info.pointName}
                                </div>
                                
                                <div className="content">
                                    {info.content}
                                </div>
                                <div className="reviewDate">
                                    {info.updated_date}
                                </div>
                                <button className="btn" onClick={onOpenModal} style={{width:"70px", backgroundColor:"white", margin:"0 0 0 5px"}}>수정</button>
                                <button className="btn" onClick={onDeleteClick}  style={{width:"70px" , backgroundColor:"white",  margin:"0 0 0 5px"}}>삭제</button>
                                {modalOn? <Modal/>: ''}
                            </div>
                            
                
                            
        </ReviewBox>
    );
}

const MyReview = ()=>{
    const getUrl = "https://www.wannawalk.co.kr:8001/maps/userlist/";
    const jwtToken = sessionStorage.getItem('jwtToken');
    const [reviews, setReviews] = useState([{content: '',
        created_date: '',
        dog_possible:'',
        id:'',
        point: '',
        pointName:'',
        updated_date: '',
        user: '',
        walkingtrails: '',}]);


    const getReviewInfos = async()=>{
        try{
            const getReviewsFromBack = await axios.get(getUrl, {
                headers: {
                    'Authorization': `Bearer ${jwtToken}`
                },
            })
            
            const addReviews = getReviewsFromBack.data.map(val=>{
                return {
                             walkingtrails: val.walkingtrails,
                             content: val.content,
                             created_date: val.created_date,
                             dog_possible:val.dog_possible,
                             id:val.id,
                             point: parseInt(val.point),
                             pointName:val.point_name,
                             updated_date: val.updated_date.slice(0,10),
                             user: val.user,
                             walkingtrails: val.walkingtrails,
                         }
            })
            setReviews(addReviews);
            
        }catch(e){
            console.log(e);
        }
    }

    useEffect(() => {
        getReviewInfos();
        
    }, []);


    return (
        <div className="main-container">
            
            <Header />
            <div className="container">
                <div className='container2'>
                    <Navigator />

                    <div class="list-wrap">
                    <div class="list" style={{marginLeft:'20px',marginTop:"10px", height:"400px",overflow:"scroll"}} >

                        {reviews.map(rev=>{
                            return <ReviewComponent key={rev.id} info={rev}></ReviewComponent>
                        })}
                        
                    </div>
                    </div>
                </div>
                
            </div>
            
        </div> 
    );
}

export default MyReview;