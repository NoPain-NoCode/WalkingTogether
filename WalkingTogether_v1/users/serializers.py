from rest_framework import serializers

from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'age_range', 'nickname', 'gender', 'profile_public', 'number_of_pet', 'warning_stack']