"""WalkingTogether_v1 URL Configuration

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
from re import I
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.views.generic import TemplateView
from rest_framework import views

from maps.views import NearRoadView, RoadDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('rest_framework.urls')),
    path('api/near_walk',NearRoadView.as_view()),
    path('api/road_detail/<int:point_number>',RoadDetailView.as_view()),
    # 리뷰 관련 뷰
    # path('review/<int:id>/',views.detail)
]