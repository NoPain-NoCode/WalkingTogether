import React , {useState, useEffect} from 'react' ;
import {Link} from 'react-router-dom';
import axios from 'axios';
import ModifyUserInfo from './ModifyUserInfo';

import Header from './Header';
import Navigator from './Navigator';

import '../style/mypageInfo.css';

import dog from '../icon/dog.png';
import UserInfo from './UserInfo';
import LikedList from './LikedList';
import profile from '../icon/profile.png';


const MyPage = ()=>{

    const jwtToken = sessionStorage.getItem('jwtToken');

    const [userInfo, setUserInfo] = useState({
        age_range: '', 
        nickname: "", 
        gender: '', 
        profile_public: true
    });
    

    useEffect(() => {
        loadUserInfo();
    },[]);

    const loadUserInfo =  async()=>{
        try{
            
            console.log(jwtToken);
            const newUserInfo = await axios.get('https://www.wannawalk.co.kr:8001/user/update',{
                headers: {
                    'Authorization': `Bearer ${jwtToken}`
                },
            })
            console.log(newUserInfo.data);
            
            setUserInfo(newUserInfo.data);

        }catch(e){
            console.log(e);
        }
    }

    return (
        <div className="main-container">
            <div className="container">
            <Header />
            {userInfo.age_range === null ? <p>안녕하세요 {userInfo.nickname}님. 서비스 이용을 위해 회원 정보를 등록 해 주세요.</p>:<p></p> }
            <div className='container2'>
                <Navigator />
                <UserInfo className="my-info"  userInfo={userInfo} />
            </div>

            
        </div>
        
        </div>
    );
}

export default MyPage;