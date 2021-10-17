import React , {useState, useEffect} from 'react' ;
import {Link} from 'react-router-dom';
import axios from 'axios';

import Header from './Header';
import Navigator from './Navigator';
import petImg from "../icon/dog.png"

const jwtToken = sessionStorage.getItem("jwtToken");



const MyPet = ()=>{
    const updateUrl = "https://www.wannawalk.co.kr:8001/user/pet/update/";
    const [petInfos, setPetInfos] = useState([]);

    const [modalOn, setModalOn] = React.useState(false); 

        const onOpenModal = () => {
            setModalOn(!modalOn);
        }
    
    const getPetInfo = async ()=>{
        const infos = await axios.get("https://www.wannawalk.co.kr:8001/user/pet/list/",{
            headers: {
                'Authorization': `Bearer ${jwtToken}`
            }});
        console.log(infos.data);
        setPetInfos(infos.data);
    }

    useEffect(() => {
        getPetInfo();
    }, []);

    const AddNewPetInfo = ()=>{
     
        const [name, setName] = useState();
        const [gender, setGender] = useState();
        const [img, setImg] = useState();
        const [introduce, setIntroduce] = useState();
    
        const formData = new FormData();
    
        const onChange = (e) => {
            setImg(e.target.files[0]);
          }
        
        const onAddSubmit = async()=>{
            const formData = new FormData();
            formData.append("pet_image", img);
            formData.append("pet_name",name);
            formData.append("gender",gender);
            formData.append("introducing_pet",introduce);
    
            const addResult = await axios.post("https://www.wannawalk.co.kr:8001/user/pet/add/",formData,{
                headers: {
                    'Authorization': `Bearer ${jwtToken}`
                }});
            console.log(addResult);
            alert('등록 완료!');
            document.location.href = '/myPet';
        }
        return(
            
            <div className="modal" >
            <div className="bg"></div>
            <div className="modalBox" >
                
                <button className="closeBtn" onClick={onOpenModal}>✖</button> 
                {/* <img className="profile" src={"http://127.0.0.1:8001"+val.pet_image} style={{width:"200px", borderRadius:"100px", marginTop:"50px"}}/> */}
                <p>반려동물 프로필 추가하기</p>
                <input name="petImage" type="file" accept="image/*" onChange={onChange}/>
                <p>반려동물 이름</p>
                <input className="userName" type="text" onChange={(e)=>setName(e.target.value)} />
    
                <p>성별</p>
                <div className="radiobox userInfo">
                    <label><input name='gender'  type='radio'  value='male' onChange={(e)=>setGender(e.target.value)}/>남</label>
                    <label><input name='gender'  type='radio'  value='female' onChange={(e)=>setGender(e.target.value)}/>여</label>
                </div>  
                <p>한줄소개</p>
                <input className="age" type="text" onChange={(e)=>setIntroduce(e.target.value)} />
                
                <button onClick={onAddSubmit}>등록하기</button>
            </div>
        </div>
            
        );
    }

    const PetInfoItem = ({val})=>{

        const [modalOn, setModalOn] = React.useState(false); 

        const onOpenModal = () => {
            setModalOn(!modalOn);
        }

        const onDelete = async ()=>{
            const deleteResult = await axios.delete(updateUrl+val.id,{
                headers: {
                    'Authorization': `Bearer ${jwtToken}`
                }});
            console.log(deleteResult);
            alert('삭제 완료!');
            document.location.href = '/myPet';
        }

        
        const ModifyPetInfo = ({val})=>{
            const updateUrl = "https://www.wannawalk.co.kr:8001/user/pet/update/";
        
            const jwtToken = sessionStorage.getItem('jwtToken');
        
            const [name, setName] = useState(val.pet_name);
            const [gender, setGender] = useState(val.gender);
            const [newImg, setNewImg] = useState(val.img);
            const [introduce, setIntroduce] = useState(val.introducing_pet);
        
            
        
            const onChange = (e) => {
                setNewImg(e.target.files[0]);
              }
        
            const onPutSubmit = async()=>{
                const formData = new FormData();
                formData.append("pet_image", newImg);
                formData.append("pet_name",name);
                formData.append("gender",gender);
                formData.append("introducing_pet",introduce);
        
                const putResult = await axios.put(updateUrl+val.id+"/",formData,{
                    headers: {
                        'Authorization': `Bearer ${jwtToken}`
                    }});
                console.log(putResult);
                alert('수정 완료!');
                document.location.href = '/myPet';
            }

            
            return (
                <div className="modal" >
                    <div className="bg"></div>
                    <div className="modalBox">
                        <button className="closeBtn" onClick={onOpenModal}>✖</button> 

                        <p>반려동물 프로필 수정하기</p>
                        <img className="profile" src={"https://www.wannawalk.co.kr:8001"+val.pet_image} style={{width:"200px", borderRadius:"100px"}}/>
                        <p>반려동물 사진</p>
                        <input name="petImage" type="file" accept="image/*" onChange={onChange}/>
                        <p>반려동물 이름</p>
                        <input className="userName" type="text" onChange={(e)=>setName(e.target.value)} />
        
                        <p>성별</p>
                        <div className="radiobox userInfo">
                            <label><input name='gender'  type='radio'  value='male' onChange={(e)=>setGender(e.target.value)}/>남</label>
                            <label><input name='gender'  type='radio'  value='female' onChange={(e)=>setGender(e.target.value)}/>여</label>
                        </div>  
        
                        <p>한줄소개</p><input className="age" type="text" onChange={(e)=>setIntroduce(e.target.value)} />
                        
                        <button onClick={onPutSubmit}>수정 완료</button>
                    </div>
                </div>
                
            );
        }
    
        return (
            <div>
                <img className="profile" src={val.pet_image!=null ? "https://www.wannawalk.co.kr:8001"+val.pet_image:petImg} style={{width:"200px", hight:"200px",borderRadius:"100px"}}/>
                <div className="userName">{val.pet_name}</div>
                <div className="gender">{val.gender}</div>
                <div className="age">{val.introducing_pet}</div>
                <button className="btn" onClick={onOpenModal} style={{width:"70px"}}> 수정</button>
                {modalOn? <ModifyPetInfo val={val} />:''}
                <button className="btn" onClick={onDelete} style={{width:"70px"}}>삭제</button>
            </div>
        );
    }
     
     
     

    return(
        <div className="main-container">
            <div className="container">
                <Header />
                <div className='container2'>
                    <Navigator />
                    <div className="pet-container" style={{display: "grid",gridTemplateColumns: "repeat(2, 1fr)",marginTop: "5px",height: "500px",overFlow: "scroll"}}>
                        
                            {petInfos.map(val=>{
                                return <div className="pet-info" > <PetInfoItem val={val} ></PetInfoItem> </div>
                                
                            })}
                            {petInfos.length < 2 ? <button  onClick={onOpenModal} className="btn" style={{margin:"100px 0 0 100px"}} >반려동물 추가</button> : ''}
                            {modalOn? <AddNewPetInfo />:''}
                       
                    </div>
                </div>
            </div>
        </div>
    );
    
}

export default MyPet; 