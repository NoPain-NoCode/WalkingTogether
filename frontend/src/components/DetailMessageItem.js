import React from 'react';


const DetailMessageItem = ({val , direction})=>{
    
    return (
        <div style={direction==="left" ? {backgroundColor:"white", marginBottom:"5px"}: {backgroundColor:"#fbecc3", marginBottom:"5px"}}>
            <div >
                <div style={direction==="left" ? {textAlign:"left"}: {textAlign:"right"}}>{val.content}</div>
                <div >
                    <div style={direction==="left" ? {textAlign:"left"}: {textAlign:"right"}}>{val.datetime.slice(2,10)} {val.datetime.slice(11,16)}</div>
                </div>
            </div>
        </div>
    )
}

export default DetailMessageItem ;