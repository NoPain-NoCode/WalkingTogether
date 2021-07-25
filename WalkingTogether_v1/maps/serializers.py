from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import WalkingTrails

class WalkingTrailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = WalkingTrails
        fields = '__all__'