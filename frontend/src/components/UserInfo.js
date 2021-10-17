import React ,{useState, useEffect} from 'react';
import axios from 'axios';
import {Link} from 'react-router-dom';
import postUserInfoURL from '../api/client'
import {useForm} from 'react-hook-form';
import client from '../api/client';
import profile from '../icon/profile.png';
import dog from '../icon/dog.png';
import GlobalStyles from './GlobalStyles';
import ModifyUserInfo from './ModifyUserInfo';

const UserInfo = ({userInfo})=>{

    const [modalOn, setModalOn] = React.useState(false); 

    const onOpenModal = () => {
        setModalOn(!modalOn);
    }
    console.log(userInfo);

    const ModifyUserInfo = ({val}) =>{
        const jwtToken = sessionStorage.getItem('jwtToken');
    
    
        const [userInfo, setUserInfo] = useState({
            age_range: val.age_range, 
            nickname: val.nickname, 
            gender: val.gender, 
            profile_public: val.profile_public
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
    
        
    
        const onChange = (e)=>{
            let {name, value} = e.target;
            if (name === 'profile_public'){
                if(!e.target.checked){
                    value = false;
                }
                else{
                    value = true;
                }
            }
            setUserInfo({
                ...userInfo,
                [name]:value,
            });
        }
        const onSubmit = async ()=>{
            try{
                console.log(userInfo);
                alert('수정 완료');
                const newUserInfo = await axios.put('https://www.wannawalk.co.kr:8001/user/update/',userInfo,{
                    headers: {
                        'Authorization': `Bearer ${jwtToken}`
                    },
                })
                console.log(newUserInfo);
                document.location.href = '/myPage';
            }catch(e){
                console.log(e);
            } 
        }
        
    
        return(
    
            
            <div className="modal">
                <div className="bg"></div>
                <div className="modalBox" style={{height:"400px"}}>
                    <button className="closeBtn" onClick={onOpenModal}>✖</button> 
                    <div className="edit-box">
                
                        <div className='title'>프로필 수정</div>
    
                            <div className='user-info-box'>
                                <p>닉네임</p>
                                <input className="userName userInfo" name='nickname'  placeholder={userInfo.nickname} onChange={onChange}/>
    
                                <p>성별</p>
                                <div className="radiobox userInfo">
                                    <label><input name='gender'  type='radio'  value='male' onChange={onChange}/>남</label>
                                    <label><input name='gender'  type='radio'  value='female' onChange={onChange}/>여</label>
                                </div>  
    
                                <p>나이</p>
                                <div className='form-group userInfo-first'>
                                <select className="form-select" id='exampleSelect1' name='age_range' onChange={onChange}>
                                    <option value='null'>나이를 선택 해 주세요.</option>
                                    <option value='10~19'>10대</option>
                                    <option value='20~29'>20대</option>
                                    <option value='30~39'>30대</option>
                                    <option value='40~49'>40대</option>
                                    <option value='50~59'>50대</option>
                                    <option value='60~69'>60대</option>
                                    <option value='70~79'>70대</option>
                                    <option value='80~89'>80대</option>
                                </select>
                                   
                            </div>
    
                            <p>프로필 공개 여부</p>
                                    <div className='radiobox userInfo'>
                                        <label><input name='profile_public' type='checkbox'  value='true' onChange={onChange}/>프로필 공개 허용 여부</label>
                                    </div>
                        </div>
                        
                    
                 
            
                    </div>
                    
    
                    <button className='btn' onClick={onSubmit}>수정 완료</button>
                </div>    
                
            </div>
            
        );
    }



    return (
        
        
                <div>
                    
                    <img className="profile" src={profile} alt="../img/icon/profile.png"/>
                        <div className="userName">{userInfo.nickname} 님</div>
                        <div className="age"> {userInfo.age_range === null ? '나이를 입력 해 주세요 ': userInfo.age_range} </div>
                        <div className="gender"> {userInfo.gender===null ? '성별을 입력 해 주세요':(userInfo.gender==='female'?'여자':'남자')}</div>
                        <div>프로필 공개 동의 여부 : {userInfo.profile_public ? '동의':'비동의'}</div>
                        <button className="btn" onClick={onOpenModal} style={{width:"70px"}}> 수정</button>
                        {modalOn? <ModifyUserInfo val={userInfo} />:''}
                </div>
                    

                
        
        
    );
}  

export default UserInfo;