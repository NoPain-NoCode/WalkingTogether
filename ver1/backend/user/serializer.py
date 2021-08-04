from rest_framework import serializers

from .models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserInfoUpdateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["age_range", "nickname", "gender", "profile_public"]