"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import urls
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

import user.views
import maps.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user.views.home, name='home'),
    # jwt token
    path('api-jwt-auth/', obtain_jwt_token),          # JWT 토큰 획득
    path('api-jwt-auth/refresh/', refresh_jwt_token), # JWT 토큰 갱신
    path('api-jwt-auth/verify/', verify_jwt_token),   # JWT 토큰 확인
    # rest-auth
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    # accounts
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('dj_rest_auth.urls')),
    # my apps include
    path('user/', include('user.urls')),
    path('maps/', include('maps.urls')),
    path('msg/', include('message.urls')),
    #rest-api
    path('api/',include('rest_framework.urls')),
    path('api/near_walk',maps.views.NearRoadView.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
