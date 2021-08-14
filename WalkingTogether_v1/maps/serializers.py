from rest_framework import serializers

from .models import WalkingTrails, Review

class PointSerializer(serializers.ModelSerializer):
    class Meta:
        model = WalkingTrails
        fields = ('latitude', 'longitude')
class WalkingTrailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = WalkingTrails
        fields = '__all__'

class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'