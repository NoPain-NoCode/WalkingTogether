const CLIENT_ID = process.env.REACT_APP_KAKAO_KEY;

// const CLIENT_ID = "d4945fc79c2c3152f29bd65872586b13";
const REDIRECT_URI =  "https://www.wannawalk.co.kr:3001/oauth/callback/kakao/";

export const KAKAO_AUTH_URL = `https://kauth.kakao.com/oauth/authorize?client_id=${CLIENT_ID}&redirect_uri=${REDIRECT_URI}&response_type=code`;