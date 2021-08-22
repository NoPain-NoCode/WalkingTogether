from django.urls import path
from .views import *

app_name = 'maps'

urlpatterns=[
    # 산책로
    path('near_road',NearRoadView.as_view()), # 산책로 리턴
    path('road_detail/<int:point_number>',RoadDetailView.as_view()),
    # review
    path('review/list/<int:point_number>',ReviewListAPIView.as_view()),
    path('review/add/<int:point_number>',ReviewAddAPIView.as_view()),
    path('review/update/<int:pk>/',ReviewDetailAPIView.as_view()),
]