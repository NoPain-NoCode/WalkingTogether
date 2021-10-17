import React from 'react';
import axios from 'axios';

const LikedList = ()=>{

    const jwtToken = sessionStorage.getItem('jwtToken');
    const getList = async ()=>{
        const liked = await axios.get('https://www.wannawalk.co.kr:8001/user/liketraillist/',{
            headers: {
                'Authorization': `Bearer ${jwtToken}`
            },
            })

        console.log(liked.data);
        return (
            <div>좋아요 리스트{liked.data}</div>
        );
    };
}

export default LikedList;