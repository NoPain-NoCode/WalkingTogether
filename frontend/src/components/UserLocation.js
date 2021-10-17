import React , {useState,useEffect} from 'react';
import axios from 'axios';

const UserLocation =()=>{
    const [users,setUsers] = useState(null);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);
    const [ currentPosition, setCurrentPosition ] = useState({});
    useEffect(()=>{
        const fetchUsers = async ()=>{
            try{
                setError(null);
                setUsers(null);
                setLoading(null);
                const response = await axios.get(
                    'https://jsonplaceholder.typicode.com/users'
                );
                setUsers(response.data);
            }catch(e){
                setError(e);
            }
            setLoading(false);
        };
        fetchUsers();
    },[]);

    if (loading) return <div>로딩중..</div>;
    if(error) return <div>에러 발생</div>
    if(!users) return null;
    return (
        <ul>
            {users.map(user=>(
                <li key={user.id}>
                    {user.username} ({user.name})
                </li>
                ))
            }    
            
        </ul>
    );
}

export default UserLocation;