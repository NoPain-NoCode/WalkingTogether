from re import I
from django.db.models.fields import json
from django.http import request
from django.http.response import JsonResponse
from django.shortcuts import render
from django.db.models import Q, fields
from django.views.generic.base import View

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404

# from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework import generics, mixins
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import permissions

from django.views.decorators.csrf import csrf_protect

from .serializers import WalkingTrailsSerializer, ReviewSerializer, PointSerializer
from .form import PostForm

from haversine import haversine
from decimal import Decimal

from .models import WalkingTrails, Review

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

# 위경도로 범위 구해서 리턴하는 함수
# @csrf_protect
# @api_view(['GET'])
@permission_classes([permissions.AllowAny,])
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
    permission_classes = (permissions.AllowAny,)

    def __init__(self):
        self.point = (37.4669357, 126.9478376)
    
    def get_queryset(self):
        print("getqueryset 들어옴")
        try:
            # 현재 위치 정보 받아오기
            # longitude = float(request.GET.get('longitude',None))
            # latitude = float(request.GET.get('latitude',None))
            point = self.point

            latitude = point[0]
            longitude = point[1]
            
            # 임시 위경도
            # longitude = 126.9478376
            # latitude = 37.4669357

            near_road = getBound(latitude,longitude)
        except:
            near_road = WalkingTrails.objects.all()
        
        return near_road
    
    def get(self, request, *args, **kwargs):
        print("get")
        try:
            print("get 들어옴")
            lng = request.GET.get('lng')
            lat = request.GET.get('lat')
            self.point = (lng,lat)
            print("get성공")
        except:
            print("get안함")
            pass
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            print('post 들어옴')
            data = JSONParser().parse(request)
            latitude = data['lat']
            longitude = data['lng']
            try:
                near_road = getBound(latitude,longitude)
                serializer = WalkingTrailsSerializer(near_road, many=True)
            except:
                near_road = WalkingTrails.objects.all()
                serializer = WalkingTrailsSerializer(near_road, many=True)
                
        return Response(serializer.data)


# 리뷰 관련 뷰
# class ReviewViewSet(viewsets.ModelViewSet):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

class ReviewView(View):

    # 리뷰 작성
    @login_required
    def post(self, request):

        try:
            data = json.loads(request.body)
            user = request.user

            content = data.get('content', None)

            post_point = data.get('post_point', None)

            if not content and post_point:
                return JsonResponse({'message':'KEY_ERROR'}, status=400)
            
            review = Review.objects.create(
                content=content,
                post_point=post_point,
                user_id=user.id,
            )
        
        except:
            return
    
    # 리뷰 조회
    def get(self, request):

        reviews = Review.objects.all()

        result = []
        for review in reviews:
            review_info = {
                'comment': review.content,
                'point_id':review.point_id,
                'create_date':review.create_date,
            }

            result.append(review_info)
        
        return JsonResponse({'message':'SUCCESS', 'comment':result},status=200)