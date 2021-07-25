from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import WarlkingTrails

class WalkingTrailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = WarlkingTrails
        fields = '__all__'