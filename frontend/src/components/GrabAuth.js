import React, {useEffect} from 'react';
import axios from 'axios';

const GrabAuth = ()=>{
    let auth_code = new URL(window.location.href).searchParams.get("code");
    const url = 'https://www.wannawalk.co.kr:3001/oauth/callback/kakao/';

    const getAccessToken = async ()=>{
         try{
             const response = await axios.post(`https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id=0c2534c60e7dfcff0845164d81ab90aa&redirect_uri=${url}&code=${auth_code}`,{});
             const accessToken = response.data.access_token;
             console.log(accessToken);
            
             getUserInfo(accessToken);
         } catch (e){
             console.log(e);
         }
     }

     const getUserInfo = async (accessToken)=>{
         try{
             const userInfo = await axios.get('https://www.wannawalk.co.kr:8001/user/login/kakao/',{
                 headers: {
                     'Authorization': `Bearer ${accessToken}`
                 },
             })
             console.log(userInfo.data.token);

             sessionStorage.setItem('jwtToken',userInfo.data.token);
             sessionStorage.getItem('jwtToken');
            
             document.location.href = '/';
         } catch(e){
             console.log(e);
         }
     }
    
     getAccessToken();

    
    return (
        <div>로그인 중입니다. </div>

    );
}

export default GrabAuth;