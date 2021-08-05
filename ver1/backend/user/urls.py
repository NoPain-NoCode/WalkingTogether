from django.urls import path
from .views import GoogleLogin, KakaoLoginView, GoogleLoginView

app_name = 'user'

urlpatterns = [
    path('rest-auth/google/', GoogleLogin.as_view(), name='google_login'),
    path('login/kakao/',KakaoLoginView.as_view(), name='kakao_login_view'),
    path('login/google/',GoogleLoginView.as_view(), name='google_login_view'),
]