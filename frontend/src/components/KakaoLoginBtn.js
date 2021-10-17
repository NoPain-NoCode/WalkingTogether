import axios from 'axios';
import React,{useState, Link} from 'react';
import kakaoLogin from '../icon/kakao_login_medium_narrow.png';
import {KAKAO_AUTH_URL} from '../api/OAuth';


const KakaoLoginBtn = ()=>{
    
    return (
        <a href={KAKAO_AUTH_URL} >
            <img  src={kakaoLogin}/>
        </a>
        
            
    );
}   

export default KakaoLoginBtn;