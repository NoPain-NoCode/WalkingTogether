import React ,{useState} from 'react';
import postUserInfoURL from '../api/client'
import {useForm} from 'react-hook-form';
import client from '../api/client';


const UserInfo = ()=>{
    const [age,setAge] = useState();
    const [userName, setUserName] = useState();
    const [gender,setGender] = useState();
    const [allow,setAllow] = useState();

    const onChange = (e)=>{
        setUserName(e.target.value)
    }
    const onSubmit = async (e)=>{
        try{
            e.preventDefault();
            const data = {
                age,
                userName,
                gender,
                allow,
            };
            console.log(data);
            await client.post('/users/update/api', data);
        }catch(e){
            console.log(e);
        }
    }
    
    return (
        
        <form onSubmit={onSubmit}>
            <select name='age' onChange={(e)=>setAge(e.target.value)}>
                <option value='10대'>10대</option>
                <option value='20대'>20대</option>
                <option value='30대'>30대</option>
                <option value='40대'>40대</option>
                <option value='50대'>50대</option>
                <option value='60대이상'>60대이상</option>
            </select>
            <input name='userName' onChange={(e)=>setUserName(e.target.value)}/>
            
            <label><input name='gender'  type='radio'  value='남' onChange={(e)=>setGender(e.target.value)}/>남</label>
            <label><input name='gender'  type='radio'  value='여' onChange={(e)=>setGender(e.target.value)}/>여</label>
            
            
            <label><input name='allow' type='checkbox'  value='true' onChange={(e)=>setAllow(e.target.value)}/>프로필 공개 허용 여부</label>
            <button type='submit'>프로필 등록 </button>
        </form>
        
    );
}  

export default UserInfo;