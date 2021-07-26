from re import I
from django.http import request
from django.shortcuts import render
from django.db.models import Q, fields
# from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework import generics, mixins

from .serializers import WalkingTrailsSerializer

from haversine import haversine
from decimal import Decimal
from .models import WalkingTrails


# 위경도로 범위 구해서 리턴하는 함수
def getBound(lat, lng):
    position = (lat, lng)
    # 반경 2km 기준 정보
    lat_x = Decimal(lat - 0.01)
    lat_y = Decimal(lat + 0.01)
    lng_x = Decimal(lng - 0.015)
    lng_y = Decimal(lng + 0.015)
    condition = (
        Q(latitude__range = (lat_x, lat_y)) |
        Q(longitude__range = (lng_x, lng_y))
    )

    # DB에서 산책로 불러와 반경 2km를 road_infos에 저장
    road_infos = (
        WalkingTrails.objects.filter(condition)
    )

    # 반경 2km내의 산책로
    near_road_infos = [info.point_number for info in road_infos 
                        if haversine(position, (info.latitude, info.longitude)) <= 2]
    result = WalkingTrails.objects.filter(point_number__in = near_road_infos)
    return result


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
