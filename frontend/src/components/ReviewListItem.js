import React from 'react';

const ReviewListItem = ({content,point,dogPossible,date})=>{
    const stars = '★'.repeat(point);
    const possible = dogPossible=='ok' ? '가능해요' : dogPossible=='dontKnow' ? '모르겠어요' : '불가능해요'; 
    return (
        <div className="comments" >
            <div className="cmt-left">
                <div className="user-name"></div>
                    <div className="grade">{stars}</div>
                </div>
                <div className="cmt-right">
                <div>반려동물 동반 가능 여부: {possible}</div>
                <div>{content}</div>

                <div className="time">{date}</div>
            </div>
        </div>
    );
}

export default ReviewListItem;