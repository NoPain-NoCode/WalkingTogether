import React from 'react';
import {Link, Route , BrowserRouter} from 'react-router-dom';
import '../style/login.css'

import logo from '../icon/logo.png';


import GrabAuth from './GrabAuth';


import KakaoLoginBtn from './KakaoLoginBtn';
import GoogleLoginBtn from './GoogleLoginBtn';
const LoginTemplate = ()=>{

    return (
        
        <div className="wrap">
                <img src={logo} className="logo" style={{marginTop:"80px"}}></img>
                <div className="wannawalk-logo">산책갈까?</div>
            
                <div className="sns">SNS계정으로 간편 로그인/회원가입</div>
                <div className="sns-login">
                        <KakaoLoginBtn className="sns-icon"/>
                        <GoogleLoginBtn className="sns-icon"/>
                    
                </div>
                
                
                
                    
                
        </div>
            
            
        
    
    );
    
}

export default LoginTemplate;