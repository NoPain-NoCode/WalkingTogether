import axios from 'axios';
import React, { useEffect, useState } from 'react';
import DetailMessageItem from './DetailMessageItem';
import Header from './Header';
import Navigator from './Navigator';

const MyMessage = ()=>{
    const jwtToken = sessionStorage.getItem("jwtToken");

    const [myMsg, setMyMsg] = useState([]);

    


    const getMyMsg = async ()=>{
        try{
            const myMsgList = await axios.get("https://www.wannawalk.co.kr:8001/msg/list/last/",{
                headers: {
                    'Authorization': `Bearer ${jwtToken}`
                },
            });
            console.log(myMsgList.data);
            let cnt = 1;
            
            setMyMsg(myMsgList.data.map(val => {
                return {
                    id:cnt++,
                    sender: val.sender.nickname,
                    receiver: val.receiver.nickname,
                    room: val.room,
                    content: val.content,
                    datetime: val.datetime.slice(2,10),
                };
            }));
            
        }catch(e){
            console.log(e);
        }
        
    }

    const MessageListItem = ({val})=>{
        const [modalOn, setModalOn] = useState(false); 
        
        const [infoMessage, setInfoMessage] = useState([]);
        const [petInfo, setPetInfo] =useState([]);
        
        const [owner, setOwner] = useState('');
        const [ownerEmail, setOwnerEmail] = useState('');
        

        

        const messageOnClick = async()=>{
            try{
                const getInfoMessage = await axios.get("https://www.wannawalk.co.kr:8001/msg/list/detail/"+val.room+'/', {headers: {
                    'Authorization': `Bearer ${jwtToken}`
                }},)
                console.log(getInfoMessage.data);
                setInfoMessage(getInfoMessage.data);
            }catch(e){
                console.log(e);
            }
        }

        const getPetsInfo = async ()=>{
            try{
                const getInfo = await axios.get("https://www.wannawalk.co.kr:8001/msg/list/detail/"+val.room+'/otheruser/petinfo/', {headers: {
                    'Authorization': `Bearer ${jwtToken}`
                }},)
                console.log(getInfo.data);
                setPetInfo(getInfo.data.map(val=>{return {"id": val.id,
                "pet_name": val.pet_name,
                "gender": val.gender,
                "pet_image": val.pet_image,
                "introducing_pet": val.introducing_pet}}));
            }catch(e){
                console.log(e);
            }
        }

        const getOwnerInfo = async ()=>{
            try{
                const getOwner = await axios.get("https://www.wannawalk.co.kr:8001/msg/room/"+val.room+'/partner/nickname/', {headers: {
                    'Authorization': `Bearer ${jwtToken}`
                }},)
                console.log(getOwner.data);
                setOwner(getOwner.data.nickname);
                setOwnerEmail(getOwner.data.email);
            }catch(e){
                console.log(e);
            }
        }

        const onOpenModal = () => {
            setModalOn(!modalOn);
            
            
            if(!modalOn){
                messageOnClick();
                getPetsInfo();
                getOwnerInfo();
            }
        }
        const MessageModal =  ()=>{
            const jwtToken = sessionStorage.getItem("jwtToken");
            const [msg, setMsg] = useState("");
            const onChange = (e)=>{
                setMsg(e.target.value);
                console.log(msg);
            }
            const postToBackMsg = async()=>{
            
            try{
                const postToMsg = await axios.post("https://www.wannawalk.co.kr:8001/msg/send/",{
                    "receiver": ownerEmail,
                    "content": msg
                },{
                    headers: {
                        'Authorization': `Bearer ${jwtToken}`
                    },
                })
                console.log(postToMsg);
                alert("쪽지를 보냈어요! 내 쪽지함을 확인 해 주세요.");
                document.location.href = '/myMessage';
            }
            catch(e){
                console.log(e);
            }
        }
            
                const getOthersName =  axios.get("https://www.wannawalk.co.kr:8001/msg/room/"+val.room+"/info/",{
                    headers: {
                        'Authorization': `Bearer ${jwtToken}`
                    },
                } );
                console.log(getOthersName.data);
            
            
            const left="left";
            const right = "right";
            return (
                <div className="modal" >
                        <div className="bg"></div>
                        <div className="modalBox">
                            <button className="closeBtn" onClick={onOpenModal}>✖</button>
                            <div style={{width:"400px", margin: "0 auto", textAlign:"center"}}>
                                <div>{owner}님의 반려동물</div>
                                <p>{petInfo.map(val=><div>{val.pet_name}, {val.gender}, {val.introducing_pet}</div>)}</p>
                            </div>
                            
                            <div className="messageListWrap" style={{height:"400px", overflow:"scroll"}}>
                                {infoMessage.map(val=> val.sender.nickname===owner ? <DetailMessageItem val={val} direction={left}></DetailMessageItem> :  <DetailMessageItem val={val} direction={right}></DetailMessageItem>)}
                            </div>
                            <input  placeholder="쪽지로 만남 신청을 해 보세요!" onChange={onChange} style={{width:"320px"}}/>
                            <button onClick={postToBackMsg} className="btn" style={{width:"50px"}}>전송</button>
                        </div>
                </div>
            );
        }
        const [mainOwner, setmainOwner] = useState('');
        const getmainOwnerInfo = async ()=>{
            try{
                const getmainOwner = await axios.get("https://www.wannawalk.co.kr:8001/msg/room/"+val.room+'/partner/nickname/', {headers: {
                    'Authorization': `Bearer ${jwtToken}`
                }},)
                console.log(getmainOwner.data);
                setmainOwner(getmainOwner.data.nickname);
            }catch(e){
                console.log(e);
            }
        }
        useEffect(() => {
            getmainOwnerInfo();
        }, [])
        return(
            <div className="box" style={{width:"340px", margin: "5px auto",}}>
                <div className="info">
                    <div >
                        <div className="path_name">
                            {mainOwner}
                        </div>
                        <div className="path_address" style={{width:"200px"}}>
                            {val.content}
                        </div>
                    </div>
                    
                    
                    {modalOn ?<MessageModal ></MessageModal> :''}
                </div>
                <button className="btn" onClick={onOpenModal} style={{backgroundColor:"white", float:"right", width:"80px"}}>쪽지 확인</button>
            </div>
        );
        
    }
    useEffect(() => {
        getMyMsg();
        
    }, []);

    return(
        <div className='main-container'>
            <div className='container'>
                <Header />
                <div className = "container2">
                <Navigator />
                <div className="list" style={{marginLeft:"10px", marginTop:"10px", overflow:"scroll", height:"400px"}}>
                    {myMsg.map(val => <MessageListItem val={val}></MessageListItem>)}
                </div>
                
                </div>
                
            </div>
        </div>
    );

}

export default MyMessage;