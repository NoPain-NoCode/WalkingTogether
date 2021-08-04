from django.shortcuts import render

from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from django.views.generic.base import View
from rest_auth.registration.views import SocialLoginView
from rest_auth.utils import jwt_encode
import requests
from django.http import JsonResponse

from .models import User, SocialPlatform
from .serializer import UserSerializer, UserInfoUpdateSerializer

# Create your views here.
def home(request):
    return render(request, 'home.html')

    
class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter


class KakaoLoginView(View): #카카오 로그인

    def get(self, request):
        access_token = request.headers["Authorization"]
        headers = ({"Authorization" : f"Bearer {access_token}"})
        url = "https://kapi.kakao.com/v2/user/me" # Authorization(프론트에서 받은 토큰)을 이용해서 회원의 정보를 확인하기 위한 카카오 API 주소
        response = requests.request("POST", url, headers=headers) # API를 요청하여 회원의 정보를 response에 저장
        user = response.json()
        print(user)

        if User.objects.filter(social_login_id=user['id']).exists(): #기존에 소셜로그인을 했었는지 확인
            user_info = User.objects.get(social_login_id=user['id'])
            # encoded_jwt = jwt.encode({'id': user_info.id}, wef_key, algorithm='HS256') # jwt토큰 발행

            return JsonResponse({ #jwt토큰, 이름, 타입 프론트엔드에 전달
                'access_token' : access_token,
                'user_info'    : user_info
            }, status = 200)            
        else:
            new_user_info = User(
                social_login_id = user['id'],
                social = SocialPlatform.objects.get(platform ="Kakao"),
                nickname = user['properties'].get('nickname'),
                email = user['kakao_account'].get('email'),
                age_range = user['kakao_account'].get('age_range'),
                gender = user['kakao_account'].get('gender')
            )
            new_user_info.save()
            # encoded_jwt         = jwt_encode.encode({'email': user_info.email}, access_token, algorithm='HS256') # jwt토큰 발행
            none_member_type    = 1
            return JsonResponse({
                'access_token' : access_token,
                'user_info'    : new_user_info
                }, status = 200)