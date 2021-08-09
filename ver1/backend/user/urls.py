from django.urls import path
from .views import KakaoLoginView, GoogleLoginView, UserInfoUpdateView

app_name = 'user'

urlpatterns = [
    path('login/kakao/',KakaoLoginView.as_view(), name='kakao_login_view'),
    path('login/google/',GoogleLoginView.as_view(), name='google_login_view'),
    path('update/', UserInfoUpdateView.as_view(), name='user_info_update_view'),
]