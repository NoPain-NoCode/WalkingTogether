import axios from 'axios';
import React, { useState, useEffect, Children } from "react";
import styled from 'styled-components';
import Header from './Header';
import NullImg from '../icon/dog.png'

const PetList = ()=>{
    const jwtToken = sessionStorage.getItem("jwtToken");
    const ListItemWrap = styled.div`
        
        background-color: var(--main-bg-color);
	    border-radius: 15px;
	    width: 300px;
	    height: 60px;
        padding:10px;
        margin-bottom: 10px;
    `;
    const [pets,setPets] = useState([]);
    
    const getPetList = async ()=>{
        try{
            const pets = await axios.get("https://www.wannawalk.co.kr:8001/user/pet/list/profilepublic/",{
                headers: {
                    'Authorization': `Bearer ${jwtToken}`
                },
            });
            console.log(pets.data);
            setPets(pets.data);
        }catch(e){
            console.log(e);
        }
        
    }
    
    useEffect(() => {
        getPetList();
    }, []);
   
    const PetListItem = ({ name, gender, info, owner, img})=>{
        const [modalOn, setModalOn] = React.useState(false); 
        const onOpenModal = () => {
            setModalOn(!modalOn);
        }
        const InputMessage = ({name,gender,img,info,owner})=>{
            const [msg, setMsg] = useState("");

            const onChange = (e)=>{
                setMsg(e.target.value);
            }
            const postToBackMsg = async()=>{
            
                try{
                    const postToMsg = await axios.post("https://www.wannawalk.co.kr:8001/msg/send/",{
                        "receiver": owner,
                        "content": msg
                    },{
                        headers: {
                            'Authorization': `Bearer ${jwtToken}`
                        },
                    })
                    console.log(postToMsg);
                    alert("쪽지를 보냈어요! 내 쪽지함을 확인 해 주세요.");
                    
                }
                catch(e){
                    console.log(e);
                }
            }
            
            return (
                <div className="modal" >
                    <div className="bg"></div>
                    <div className="modalBox">
                        <button className="closeBtn" onClick={onOpenModal}>✖</button>
                        <div>{name}에게 쪽지 보내기</div><p>{owner}</p>
                        <img src={!img ? NullImg:"https://www.wannawalk.co.kr:8001"+img} style={{width:"80px", height:"80px", borderRadius:"100px"}}/>
                        <div>{name}</div>
                        <div>{info}</div>
                        <input placeholder="쪽지로 만남 신청을 해 보세요!" onChange={onChange}/>
                        <button className="btn" onClick={postToBackMsg} >쪽지 보내기</button>
                    </div>
                </div>
                
    
            );
        }
        

        // const openMessage = 

        
        return(
            <ListItemWrap>
                <div style={{display:'flex', justifyContent:"space-between"}}>
                    <img  src={!img ? NullImg:"https://www.wannawalk.co.kr:8001"+img} style={{width:"50px", height:"50px", borderRadius:"100px"}}/>
                    <div>
                        <div>{name}</div>
                        <div>{gender}</div>
                        <div>{info}</div>
                    </div>
                    
                    <button className="btn" onClick={onOpenModal} style={{width:"50px", backgroundColor:"white"}}>쪽지</button>
                </div>
                
                {modalOn ?  <InputMessage name={name} gender={gender} info={info} img={img} owner={owner}></InputMessage>: ''}
                
            </ListItemWrap>
        );
    }

   
    return (
        <div className='main-container'>
            <div className='container'>
                <Header />
                <div className="container3">
                    {pets.map(val=><PetListItem name={val.pet_name} gender={val.gender} info={val.introducing_pet} owner={val.owner} img={val.pet_image}></PetListItem>)}
                </div>
                
            </div>
        </div>
        
    );
}

export default PetList;