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
    
    def get_point_list(self, obj):
        li = []
        roads = WalkingTrails.objects.filter(course_name=obj.course_name)
        for road in roads:
            lng = road.longitude
            lat = road.latitude
            point = (lng, lat)
            li.append(point)
        return li
    
    class Meta:
        model = WalkingTrails
        # fields = '__all__'
        fields = ('category','region','distance','time_required','_level','subway','Transportation',
                    'course_name','course_detail','_explain','point_number','point_name',
                    'longitude','latitude','point_list')
    
    

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('walkingtrails', 'id', 'user', 'content', 'created_date', 'updated_date', 'point', 'dog_possible')