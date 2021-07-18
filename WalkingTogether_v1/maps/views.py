from django.shortcuts import render
from django.db.models import Q
from .models import WarlkingTrails
from haversine import haversine

# Create your views here.
class NearRoadView(View):
    def get(self, request):
        try:
            # 현재 위치 정보 받아오기
            # longitude = float(request.GET.get('longitude',None))
            # latitude = float(request.GET.get('latitude',None))
            # 임시 위경도
            longitude = 126.9478376
            latitude = 37.4669357
            position = (latitude, longitude)

            # 반경 2km 기준 정보
            condition = (
                Q(lat_range = (latitude - 0.01, latitude + 0.01)) |
                Q(long_range = (longitude - 0.015, longitude + 0.015))
            )

            # DB에서 산책로 불러와 road_infos에 저장
            road_infos = (
                WarlkingTrails.objects.all
            )

            # 반경 2km내의 산책로
            near_road_infos = [info for info in road_infos 
                                if haversine(position, (info.latitude, info.longitude))]
        except:
            pass

        
