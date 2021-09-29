from django.urls import path
from .views import KakaoLoginView, GoogleLoginView, UserInfoUpdateView, PetListView, ProfilePublicPetListView, PetAddView, PetInfoUpdateView, ClickLikeTrailView, ClickLikeTrailListView

app_name = 'user'

urlpatterns = [
    # user
    path('login/kakao/', KakaoLoginView.as_view(), name='kakao_login_view'),
    path('login/google/', GoogleLoginView.as_view(), name='google_login_view'),
    path('update/', UserInfoUpdateView.as_view(), name='user_info_update_view'),
    # pet
    path('pet/list/', PetListView.as_view(), name='pet_list_view'),
    path('pet/list/profilepublic/', ProfilePublicPetListView.as_view(), name='profile_public_pet_list_view'),
    path('pet/add/', PetAddView.as_view(), name='pet_add_view'),
    path('pet/update/<int:pk>/', PetInfoUpdateView.as_view(), name='pet_update_view'),
    # like walking trail
    path('clickliketrail/<int:pk>/', ClickLikeTrailView.as_view(), name='click_like_trail_view'),
    path('liketraillist/', ClickLikeTrailListView.as_view(), name='click_like_trail_list_view')
]