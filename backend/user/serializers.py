from codecs import lookup_error
from django.db.migrations.operations import fields
from rest_framework import serializers

from .models import User, Pet, UserLikeWalkingTrail
from maps.models import WalkingTrails
from maps.serializers import WalkingTrailsSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserNicknameSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'nickname']


class UserInfoUpdateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["age_range", "nickname", "gender", "profile_public"]


# 좋아요 누른 산책로 데이터
class UserLikeWalkingTrailSerializer(serializers.ModelSerializer):
    walkingtrail = WalkingTrailsSerializer(read_only=True)

    class Meta:
        model = UserLikeWalkingTrail
        fields = ["walkingtrail"]


class PetSerializer(serializers.ModelSerializer):
    pet_image = serializers.ImageField(use_url=True)

    class Meta:
        model = Pet
        fields = ["id", "pet_name", "gender", "pet_image", "introducing_pet"]


class IncludeOwnerInfoPetSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField()
    pet_image = serializers.ImageField(use_url=True)

    class Meta:
        model = Pet
        fields = ["id", "pet_name", "owner", "gender", "pet_image", "introducing_pet"]


class PetUpdateSerializer(serializers.ModelSerializer):
    pet_image = serializers.ImageField(use_url=True)

    class Meta:
        model = Pet
        fields = ["pet_name", "gender", "pet_image", "introducing_pet"]