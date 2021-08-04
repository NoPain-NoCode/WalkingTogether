import json
from django.shortcuts import render

from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from django.views.generic.base import View
from rest_auth.registration.views import SocialLoginView
from rest_auth.utils import jwt_encode
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from .models import User, SocialPlatform
from .serializer import UserSerializer, UserInfoUpdateSerializer

# Create your views here.
def home(request):
    return render(request, 'home.html')

    
class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter


@method_decorator(csrf_exempt, name='dispatch')
class KakaoLoginView(View): #카카오 로그인
    def get(self, request):
        access_token = request.headers["Authorization"]
        headers      = ({"Authorization" : f"{access_token}"})
        url          = "https://kapi.kakao.com/v2/user/me" # Authorization(프론트에서 받은 토큰)을 이용해서 회원의 정보를 확인하기 위한 카카오 API 주소
        response     = requests.request("POST", url, headers=headers) # API를 요청하여 회원의 정보를 response에 저장
        user         = response.json()
        print(user)

        if User.objects.filter(social_login_id=user['id']).exists(): #기존에 소셜로그인을 했었는지 확인
            user_info = User.objects.get(social_login_id=user['id'])
            print(user_info)
            # request.session['user'] = user_info.id
            # encoded_jwt = jwt.encode({'id': user_info.id}, wef_key, algorithm='HS256') # jwt토큰 발행

            response_data = {
                'access_token'    : access_token,
                'nickname'        : user_info.nickname,
                'email'           : user_info.email,
                'age_range'       : user_info.age_range,
                'gender'          : user_info.gender
            }
            return JsonResponse(response_data, json_dumps_params={'ensure_ascii': False}, status = 200)            
        else:
            new_user_info = User(
                social_login_id = user['id'],
                social          = SocialPlatform.objects.get(platform ="Kakao"),
                nickname        = user['properties'].get('nickname'),
                email           = user['kakao_account'].get('email'),
                age_range       = user['kakao_account'].get('age_range'),
                gender          = user['kakao_account'].get('gender')
            )
            new_user_info.save()
            # request.session['user'] = new_user_info.id
            # encoded_jwt         = jwt_encode.encode({'email': user_info.email}, access_token, algorithm='HS256') # jwt토큰 발행
            none_member_type = 1
            response_data = {
                'access_token'      : access_token,
                'nickname'          : new_user_info.nickname,
                'email'             : new_user_info.email,
                'age_range'         : new_user_info.age_range,
                'gender'            : new_user_info.gender
                }
            return JsonResponse(response_data, json_dumps_params={'ensure_ascii': False}, status = 200)