from django.urls import path
from .views import KakaoLogin, GoogleLogin

app_name = 'user'

urlpatterns = [
    path('rest-auth/kakao/', KakaoLogin.as_view(), name='kakao_login'),
    path('rest-auth/google/', GoogleLogin.as_view(), name='google_login'),
]