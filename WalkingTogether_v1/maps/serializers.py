from django.db import models
from django.db.models import fields
from django.db.models.fields import files
from rest_framework import serializers
from .models import WalkingTrails, Review

class WalkingTrailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = WalkingTrails
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'