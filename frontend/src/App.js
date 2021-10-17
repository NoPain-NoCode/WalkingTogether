import React from 'react';
import {Route, BrowserRouter} from 'react-router-dom';
import KakaoLoginBtn from './components/KakaoLoginBtn';
import MapListItem from './components/MapListItem';
// import MapContainer from './components/MapContainer';
// import MapListItem from './components/MapListItem';
import UserInfo from './components/UserInfo'
import GrabAuth from './components/GrabAuth';
import GoogleLoginBtn from './components/GoogleLoginBtn';
import LoginTemplate from './components/LoginTemplate';
import client from './api/client'
import MapContainer from './components/MapContainer'
import Home from './components/Home'
import MyPage from './components/MyPage';
import ModifyUserInfo from './components/ModifyUserInfo';
import RecommendInfo from './components/RecommendInfo';
import MyRoad from './components/MyRoad';
import MyReview from './components/MyReview';
import MyPet from './components/MyPet.js';
import ModifyPetInfo from './components/ModifyPetInfo.js';
import SearchHome from './components/SearchHome';
import PetList from './components/PetList';
import MyMessage from './components/MyMessage';

const App=()=>{
  

  return (
      <div>
        <Route path='/' component={Home} exact={true}/>
        <Route path='/login' component={LoginTemplate}/>
        <Route path='/oauth/callback/kakao/'  component={GrabAuth} />
        <Route path='/myPage' component={MyPage} />
        <Route path='/myPet' component={MyPet} />
        <Route path='/myRoad' component={MyRoad} />
        <Route path='/myReview' component={MyReview}/>
        <Route path='/detail/:pointNum' component={RecommendInfo}/>
        <Route path='/infoModify' component={ModifyUserInfo} />
        <Route path="/petInfoModify" component={ModifyPetInfo} />
        <Route path="/search/:searchKeyword" component={SearchHome}/>
        <Route path="/petList" component={PetList}/>
        <Route path="/myMessage" component={MyMessage}/>
      </div>   

    // <MapContainer />
  );
};

export default App;
