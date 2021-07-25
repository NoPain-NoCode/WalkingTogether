from django.http.response import HttpResponse
import requests
from django.shortcuts import render, redirect
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from allauth.socialaccount.models import SocialAccount
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.kakao import views as kakao_view
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from django.http import JsonResponse
from rest_framework import status
from json.decoder import JSONDecodeError
from rest_framework.response import Response

from .models import CustomUser

def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')
