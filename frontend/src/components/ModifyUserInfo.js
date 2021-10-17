import React, {useState, useEffect} from 'react';
import axios from 'axios';
import Header from './Header'
import GlobalStyles from './GlobalStyles';


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
            const newUserInfo = await axios.get('http://npnc.wannawalk.co.kr:8001/user/update',{
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
            const newUserInfo = await axios.put('http://npnc.wannawalk.co.kr:8001/user/update/',userInfo,{
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
            <div className="modalBox">
                
               
            
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
                            
                              
                
                            <p>프로필 공개 여부</p>
                                <div className='radiobox userInfo'>
                                    <label><input name='profile_public' type='checkbox'  value='true' onChange={onChange}/>프로필 공개 허용 여부</label>
                                </div>
                
                                <button className='btn' onClick={onSubmit}>수정 완료</button>
                        </div>

                    
                    </div>
                    
                
             
        
                
                


            </div>    
            
        </div>
        
    );
}

export default ModifyUserInfo;