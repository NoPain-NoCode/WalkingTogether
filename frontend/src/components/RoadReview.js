import React , {useState} from 'react';
import Fieldset from 'react-fieldset';
import axios from 'axios';
import '../style/review.css';
import { createGlobalStyle } from 'styled-components';
import reset from 'styled-reset';

import GlobalStyles from './GlobalStyles';



const RoadReview = ({pointNum,infos})=>{
    const addurl = 'https://www.wannawalk.co.kr:8001/maps/review/add/'+pointNum+'/';
    
    const jwtToken = sessionStorage.getItem('jwtToken');
    
    const [review, setReview] = useState(infos?infos.content:'');
    const [score, setScore] = useState(infos?infos.point:'');
    const [dogOk, setDogOk] = useState(infos?infos.dog_possible:'');

    const onReviewSubmit = (e) => {
        e.preventDefault();
        if (jwtToken){
            if(review && score && dogOk ){
                if(infos.content){
                    const updateUrl = 'https://www.wannawalk.co.kr:8001/maps/review/update/'+infos.id+'/';
                    axios.put(updateUrl, {
            
                        content: review,
                        point: score,
                        dog_possible: dogOk,
                        
                    }, {
                        headers: {
                            'Authorization': `Bearer ${jwtToken}`
                        }
                    })
                    .then(response => { 
                        console.log(response);
                        alert("리뷰 수정 완료!");
                        document.location.href = "/myReview"
                    })
                    .catch(error => {
                        console.log(error.response)
                    });  
                }
                else{
                    axios.post(addurl, {
            
                        content: review,
                        point: score,
                        dog_possible: dogOk,
                        
                    }, {
                        headers: {
                            'Authorization': `Bearer ${jwtToken}`
                        }
                    })
                    .then(response => { 
                        console.log(response);
                        alert("리뷰 등록 완료!");
                        document.location.href = "/detail/"+pointNum;
                    })
                    .catch(error => {
                        console.log(error.response)
                    });  
                }
            }
            else{
                alert('빈 항목 없이 작성 해주세요');
            }
        }
        else{
            alert('로그인 후 리뷰 등록이 가능해요. 로그인 해 주세요');
        }
        
    }

    return(
        <div className='wrap'>
            <GlobalStyles />
                <div className='container'>
                    <form name='score' className='myform' onChange={(e)=>setScore(e.target.value) }>
                        <fieldset>
                            <h2>별점</h2>
                            <input type="radio" name="rating" value="5" id="rate1"/><label for="rate1">⭐</label>
                            <input type="radio" name="rating" value="4" id="rate2"/><label for="rate2">⭐</label>
                            <input type="radio" name="rating" value="3" id="rate3"/><label for="rate3">⭐</label>
                            <input type="radio" name="rating" value="2" id="rate4"/><label for="rate4">⭐</label>
                            <input type="radio" name="rating" value="1" id="rate5"/><label for="rate5">⭐</label>
                        </fieldset>
                        
                    </form>
                </div>
                <div className="container">
                    <h2>강아지 산책 가능 여부 </h2>
                    <label className="box-radio-input">
                        <input type="radio" name="cp_item" value="ok" onClick={(e)=>setDogOk(e.target.value)}/>
                        <span>가능</span>
                    </label>
                    <label className="box-radio-input">
                        <input type="radio" name="cp_item" value="no" onClick={(e)=>setDogOk(e.target.value)}/>
                        <span>불가능</span>
                    </label>
                    <label className="box-radio-input">
                        <input type="radio" name="cp_item" value="dontKnow" onClick={(e)=>setDogOk(e.target.value)}/>
                        <span>잘 모르겠어요</span>
                    </label>
                </div> 
                <div className="container">
                    <h2>리뷰</h2>

                    <section className="reply-form">
                        <form>
                            <div>
                                <textarea placeholder="후기를 입력해주세요" onChange={(e)=>{setReview(e.target.value)}}>{review}</textarea>
                            </div>
                            <button className="btn-submit" onClick={onReviewSubmit}>{infos.content?"리뷰 수정":"리뷰 등록"}</button>
                        </form>
                    </section>
                </div>
                    
                    
                    
                    
            
            {/* <select name='score' onChange={(e)=>setScore(e.target.value) }>
                    <option value='5'>⭐⭐⭐⭐⭐</option>
                    <option value='4'>⭐⭐⭐⭐</option>
                    <option value='3'>⭐⭐⭐</option>
                    <option value='2'>⭐⭐</option>
                    <option value='1'>⭐</option>
                </select>
                코멘트<input name='review' onChange={(e)=>{setReview(e.target.value)}}></input>
                강아지 산책 가능 여부 
                <select name='dogOk' onChange={(e)=>setDogOk(e.target.value)}>
                    <option value='ok'>가능해요</option>
                    <option value='no'>불가능해요</option>
                    <option value='dontKnow'>잘 모르겠어요</option>
                </select>
                <button onClick={onReviewSubmit}>리뷰 등록하기</button>                */}
        </div> 
        
        
    );
}
RoadReview.defaultProps ={
    infos:{},
}
export default RoadReview;