from django.db.models import fields
from rest_framework import serializers
from .models import WalkingTrails, Review

BASE_URL = "http://203.237.169.237:8001/"

class PointSerializer(serializers.ModelSerializer):
    class Meta:
        model = WalkingTrails
        fields = ('latitude', 'longitude')

class WalkingTrailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = WalkingTrails
        fields = '__all__'

class WalkingTrailsDetailSerializer(serializers.ModelSerializer):
    point_list = serializers.SerializerMethodField(method_name='get_point_list')
    point_mean = serializers.SerializerMethodField(method_name='get_point_mean')
    dog_mean = serializers.SerializerMethodField(method_name='get_dog_mean')

    def get_point_mean(self, obj):
        total = 0
        cnt = 0
        reviews = Review.objects.filter(walkingtrails=obj.point_number)
        for review in reviews:
            point = int(review.point)
            total += point
            cnt += 1
        
        try:
            avg = round(total/cnt, 2)
        except:
            avg = 0

        return avg
    
    def get_dog_mean(self, obj):
        ok = 0
        no = 0
        dontknow = 0
        avg = dict()
        reviews = Review.objects.filter(walkingtrails=obj.point_number)
        for review in reviews:
            dog_possible = review.dog_possible
            if dog_possible == 'ok':
                ok += 1
            elif dog_possible == 'no':
                no += 1
            else:
                dontknow += 1
        
        try:
            total = ok + no + dontknow
            avg['ok'] = round(ok/total, 2)
            avg['no'] = round(no/total, 2)
            avg['dontknow'] = round(dontknow/total, 2)
        except:
            avg['ok'] = 0
            avg['no'] = 0
            avg['dontknow'] = 0

        return avg

    def get_point_list(self, obj):
        li = []
        roads = WalkingTrails.objects.filter(course_name=obj.course_name)
        for road in roads:
            lng = road.longitude
            lat = road.latitude
            point_name = road.point_name
            point_number = road.point_number
            point = (lng, lat, point_name, point_number)
            li.append(point)
        return li
    
    class Meta:
        model = WalkingTrails
        # fields = '__all__'
        fields = ('category','region','distance','time_required','_level','subway','Transportation',
                    'course_name','course_detail','_explain','point_number','point_name',
                    'longitude','latitude','point_list', 'point_mean', 'dog_mean')
    
    

class ReviewSerializer(serializers.ModelSerializer):
    point_name = serializers.SerializerMethodField(method_name='get_point_name')

    def get_point_name(self, obj):
        road = WalkingTrails.objects.get(point_number=obj.walkingtrails.point_number)
        point_name = road.point_name
        return point_name

    class Meta:
        model = Review
        fields = ('walkingtrails', 'id', 'point_name', 'user', 'content', 'created_date', 'updated_date', 'point', 'dog_possible')