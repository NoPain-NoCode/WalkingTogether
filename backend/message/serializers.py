from rest_framework import serializers

from .models import Room, Message
from user.serializers import UserInfoUpdateSerializer, UserNicknameSerializer


class RoomSerializer(serializers.ModelSerializer):
    user1 = UserInfoUpdateSerializer(read_only=True)
    user2 = UserInfoUpdateSerializer(read_only=True)

    class Meta:
        model = Room
        fields = ["user1", "user2"]


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    sender = UserNicknameSerializer(read_only=True)
    receiver = UserNicknameSerializer(read_only=True)
    room = serializers.StringRelatedField()

    class Meta:
        model = Message
        fields = ["id", "sender", "receiver", "room", "content", "datetime"]