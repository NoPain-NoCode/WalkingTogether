from re import I
from django.http import request
from django.shortcuts import render
from django.db.models import Q, fields
# from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework import generics, mixins
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from rest_framework.response import Response

from django.views.decorators.csrf import csrf_protect

from .serializers import WalkingTrailsSerializer
from .form import PostForm

from haversine import haversine
from decimal import Decimal
from .models import WalkingTrails


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


@csrf_protect
@api_view(["POST", "GET"])
def post_point(request):
    if request.method == 'POST':
        # serializer = WalkingTrailsSerializer(data=request.data)
        form = PostForm(request.POST)
        if form.is_valid():
            # 프론트에서 point 받아줌
            point = request.POST.get('currentPosition')
            return point
    else:
        form = PostForm()
    
    # Post 못받으면 임시 위경도 반환함
    return (126.9478376, 37.4669357)

# 위경도로 범위 구해서 리턴하는 함수
# 주석처리된 것 주석 풀면 getBound 함수가 적용 안됨
# @csrf_protect
# @api_view(['GET'])
@permission_classes([IsAuthenticated|ReadOnly])
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
    permission_classes = [IsAuthenticated|ReadOnly]
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
