import React, {useState} from 'react';

import logo from '../icon/logo.png';
import pin from '../icon/pin.png';
import userImage from '../icon/user.png';
import searchBtn from '../icon/searchBtn.png';
import infoIcon from '../icon/infoIcon.png';
import axios from 'axios'
import { Route , Link} from 'react-router-dom';
import '../style/header.css';
import GlobalStyles from './GlobalStyles';

const Header = ()=>{
    const [keyword, setKeyword] = useState();

    const jwtToken = sessionStorage.getItem('jwtToken');

    const onSubmit = async ()=>{
        // try{
        //     const searchResult = await axios.post('http://npnc.wannawalk.co.kr:8001/maps/road_search/',{
        //         "search":keyword
        //     })
        //     console.log(searchResult);
        // }catch(e){
        //     console.log(e);
        // }
        document.location.href = '/search/'+keyword;
        
    }
    
    

    
    return(
        <div className = 'main-container'>
            <div className='container' style={{margin:0}}>
            <div className="h-container">
                    <div className="h-container-left">
                    <button className="logoBtn"><img src={logo} id="logoBtnImg"/></button><Link to="/" style={{ color: 'inherit',textDecoration: 'none' }}><b>산책갈까?</b></Link>
                        <div className="btn-container">
                            <a href="/" className="WDBtn" style={{ color: 'inherit',textDecoration: 'none' }}><img src={pin} className="WDBtnImg"/><p>주변 산책로 다시 찾기</p></a>
                            {jwtToken? <Link to="/petList"  className="WDBtn">강아지 친구 찾기</Link> : ''}
                        </div>
                    </div>
                    <div className="h-container-right">
                       
                        
                        <div className="s-container">
                            
                            <input className="searchBox" type="text" placeholder="산책로 검색하기" onChange={(e)=>setKeyword(e.target.value)}/>
                            <p className="arrow_box">두 가지 이상의 키를 사용해 검색가능.<br/> ex) region:강서 level:1 => 강서지역 코스레벨 1 산책길 검색
                            <br/> ex) transportation:3호선 explain:은평뉴타운 => 3호선라인의 은평뉴타운 주민 산책로 추천</p>
                            <img src={searchBtn} className="searchBtn" onClick={onSubmit}></img>
                            
                            
                        </div>
                        <div className="user-container">
                            {jwtToken ?  
                            <div>
                                <Link to='/myPage' style={{ color: 'inherit',textDecoration: 'none' }}><b class="loginBtn">마이페이지</b><img src={userImage} id="mypageBtnImg"/><button className="mypageBtn"></button></Link>
                                <Link to='/myMessage' style={{ color: 'inherit',textDecoration: 'none' }}>쪽지함</Link>
                            </div>
                                :
                                <Link to='/login' style={{ color: 'inherit',textDecoration: 'none' }}><b class="loginBtn">로그인</b><button className="mypageBtn"><img src={userImage} id="mypageBtnImg"/></button></Link>}
                            
                        </div>
                    </div>
                </div>
            </div>
        </div>
        

    );

    
    
}

export default Header;