import Reac,{useState, useEffect} from 'react';
import axios from 'axios';

const ModifyUserInfo = ({val})=>{
    const updateUrl = "https//203.237.169.237:8001/user/pet/update/";

    const jwtToken = sessionStorage.getItem('jwtToken');

    const [name, setName] = useState(val.pet_name);
    const [gender, setGender] = useState(val.gender);
    const [newImg, setNewImg] = useState(val.img);
    const [introduce, setIntroduce] = useState(val.introducing_pet);

    

    const onChange = (e) => {
        setNewImg(e.target.files[0]);
      }

    const onSubmit = async()=>{
        const formData = new FormData();
        formData.append("pet_image", newImg);
        formData.append("pet_name",name);
        formData.append("gender",gender);
        formData.append("introducing_pet",introduce);

        const deleteResult = await axios.put(updateUrl+val.id+"/",formData,{
            headers: {
                'Authorization': `Bearer ${jwtToken}`
            }});
        console.log(deleteResult);
    }
    return (
        <div className="modal">
            <div className="bg"></div>
            <div className="modalBox">
                <img className="profile" src={"http://127.0.0.1:8001"+val.pet_image} style={{width:"200px", borderRadius:"100px"}}/>
                <input name="petImage" type="file" accept="image/*" onChange={onChange}/>
                <input className="userName" type="text" onChange={(e)=>setName(e.target.value)} />

                <div className="radiobox userInfo">
                    <label><input name='gender'  type='radio'  value='male' onChange={(e)=>setGender(e.target.value)}/>남</label>
                    <label><input name='gender'  type='radio'  value='female' onChange={(e)=>setGender(e.target.value)}/>여</label>
                </div>  

                <input className="age" type="text" onChange={(e)=>setIntroduce(e.target.value)} />
                
                <button onClick={onSubmit} className="btn">수정 완료</button>
            </div>
        </div>
        
    );
}

export default ModifyUserInfo;