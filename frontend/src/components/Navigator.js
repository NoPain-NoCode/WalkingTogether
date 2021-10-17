import React from 'react';
import {Link} from 'react-router-dom';
import '../style/navigator.css';

const Navigator = ()=>{

    return (
        <div className="sidebar">
            <Link to="/myPage" className="menu">내 정보</Link><hr/>
            <Link to="/myPet" href="#" class="menu">내 반려동물</Link> <hr></hr>
            <Link to="/myRoad" href="#" className="menu">찜한 산책로</Link><hr/>
            <Link to="/myReview" className="menu">내가 쓴 후기</Link><hr/>
            <Link to="/myMessage" className="menu">내 쪽지함</Link><hr/>
            <b  className="menu" onClick={()=>{sessionStorage.removeItem('jwtToken'); 
                            document.location.href = '/';}}>로그아웃</b><button className="mypageBtn" ></button>
        </div>

    );
}

export default Navigator;