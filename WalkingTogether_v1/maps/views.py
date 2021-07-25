from re import I
from django.http import request
from django.shortcuts import render
from django.db.models import Q
# from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework import generics, mixins, serializers

from .serializers import WalkingTrailsSerializer

from haversine import haversine
from .models import WalkingTrails


# 위경도로 범위 구해서 리턴하는 함수
def getBound(lat, lng):
    position = (lat, lng)
    # 반경 2km 기준 정보
    condition = (
        Q(lat_range = (lat - 0.01, lat + 0.01)) |
        Q(long_range = (lng - 0.015, lng + 0.015))
    )

    # DB에서 산책로 불러와 반경 2km를 road_infos에 저장
    road_infos = (
        WalkingTrails.objects.filter(condition)
    )

    # 반경 2km내의 산책로
    near_road_infos = {info for info in road_infos 
                        if haversine(position, (info.lat, info.lng))}
    return near_road_infos


# Create your views here.
class NearRoadView(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = WalkingTrailsSerializer
    
    def get_queryset(self):
        try:
            # 현재 위치 정보 받아오기
            # longitude = float(request.GET.get('longitude',None))
            # latitude = float(request.GET.get('latitude',None))

            # 임시 위경도
            longitude = 126.9478376
            latitude = 37.4669357

            near_road = getBound(latitude,longitude)
        except:
            near_road = WalkingTrails.objects.all()
        
        return near_road
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
