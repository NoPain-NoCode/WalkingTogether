import React,{Route} from 'react';
import GoogleLogin from 'react-google-login';
import UserInfo from './UserInfo'
import axios from 'axios';

const GoogleLoginBtn = ()=>{
    const CLIENT_ID = process.env.REACT_APP_GOOGLE_KEY;

    const errorResponse = (response)=>{
        console.log(response);
    }

    const responseGoogle = async (response) => {
        
        try{
            
            const userObj = response.profileObj;
            console.log(userObj);
            const jwtToken = await axios.post('https://www.wannawalk.co.kr:8001/user/login/google/',userObj);
            console.log(jwtToken.data.token);
            sessionStorage.setItem('jwtToken',jwtToken.data.token);
            sessionStorage.getItem('jwtToken');
            
            

            
            document.location.href = '/';
        }catch(e){
            console.log(e);
        }
    }


    
    return (
        <GoogleLogin
            clientId={CLIENT_ID}
            buttonText="Login with Google"
            onSuccess={responseGoogle}
            onFailure={errorResponse}
            
        />
        
    );
}

export default GoogleLoginBtn;