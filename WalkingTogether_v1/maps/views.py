from django.conf import UserSettingsHolder
from django.db.models import Q

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework import generics, mixins, serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import status

from django.views.decorators.csrf import csrf_protect

from .serializers import WalkingTrailsDetailSerializer, WalkingTrailsSerializer, PointSerializer, ReviewSerializer
from .form import PostForm

from haversine import haversine
from decimal import Context, Decimal
import uuid

from .models import WalkingTrails, Review

# JWT 토큰 유효성 검사 클래스 불러오기
from user.views import id_auth


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

# 위경도로 범위 구해서 리턴하는 함수
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
@method_decorator(csrf_exempt, name='dispatch')
class NearRoadView(generics.GenericAPIView, mixins.ListModelMixin):
    # permission_classes = [IsAuthenticated|ReadOnly]
    permission_classes = (permissions.AllowAny,)
    serializer_class = WalkingTrailsSerializer

    def __init__(self):
        self.point = (37.4669357, 126.9478376)
    
    def get_queryset(self):
        print("getqueryset 들어옴")
        try:
            point = self.point
            print(point)

            latitude = point[0]
            longitude = point[1]

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

# 세부 페이지 관련 뷰
class RoadDetailView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, point_number):
        point_no = point_number
        road = get_object_or_404(WalkingTrails, point_number=point_no)
        serializer = WalkingTrailsDetailSerializer(road)

        return Response(serializer.data)

# 리뷰 관련 뷰
# 리뷰 조회
@method_decorator(csrf_exempt, name='dispatch')
class ReviewListAPIView(APIView):
    
    def get(self, request, point_number):
        reviews = Review.objects.filter(walkingtrails=point_number)
        serializer = ReviewSerializer(reviews, many=True, context={'request':request})
        return Response(serializer.data)

# 유저가 작성한 리뷰 조회
@method_decorator(csrf_exempt, name='dispatch')
class UserReviewListAPIView(APIView):
    
    @id_auth
    def get(request):
        user = request.user
        reviews = Review.objects.filter(user=user)
        serializer = ReviewSerializer(reviews, many=True, context={'request':request})
        return Response(serializer.data)

# 리뷰 작성
@method_decorator(csrf_exempt, name='dispatch')
class ReviewAddAPIView(APIView):

    @id_auth
    def post(request, point_number,format=None):
        user = request.user
        road = WalkingTrails.objects.get(point_number=point_number)
        serializer = ReviewSerializer(data=request.data, context={'request':request})
        if serializer.is_valid():
            serializer.user = user.email
            serializer.walkingtrails = road.point_number
            serializer.save(user=user, walkingtrails=road)
            # road.count_review += 1
            # road.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 하나의 리뷰 내용, 수정, 삭제
@method_decorator(csrf_exempt, name='dispatch')
class ReviewDetailAPIView(APIView):

    def get(self, request, pk, format=None):
        review = Review.objects.get(id=pk)
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    
    @id_auth
    def put(request, pk):
        # review = Review.objects.filter(id=pk)
        user = request.user
        review = Review.objects.get(id=pk)
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid():    
            if str(review.user) == str(user.email):
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_403_FORBIDDEN)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @id_auth
    def delete(request, pk):
        user = request.user
        review = Review.objects.get(id=pk)
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(): 
            if str(review.user) == str(user.email):
                review.delete()
                # road.count_review -= 1
                # road.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
            return Response(serializer.errors, status=status.HTTP_403_FORBIDDEN)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

