import re
from django.core.checks import messages
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponse
from django.db.models import Q
from rest_framework import serializers, status
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import MessageSerializer, RoomSerializer
from .models import Room, Message
from user.models import User, Pet
from user.views import id_auth
from user.serializers import PetSerializer, UserNicknameSerializer

# Create your views here.

@method_decorator(csrf_exempt, name='dispatch')
class SendMessageView(APIView):

    @id_auth
    def post(request, format=None):
        sender = request.user
        receiver_email = request.data['receiver']
        content = request.data['content']
        receiver = User.objects.get(email=receiver_email)

        # 이미 쪽지한 적이 있으면 기존의 room에 저장
        if Room.objects.filter(Q(user1=sender) & Q(user2=receiver)).exists():
            room = Room.objects.get(Q(user1=sender) & Q(user2=receiver))
        elif Room.objects.filter(Q(user1=receiver) & Q(user2=sender)).exists():
            room = Room.objects.get(Q(user1=receiver) & Q(user2=sender))
        # 처음 쪽지하는 것이라면 room 생성 후, 생성한 room에 저장
        else:
            room = Room(
                user1 = sender,
                user2 = receiver
            )
            room.save()
        
        message = Message(
            sender = sender,
            receiver = receiver,
            room = room,
            content = content
        )
        message.save()
        return HttpResponse(status=201)


@method_decorator(csrf_exempt, name='dispatch')
class DeleteMessageView(APIView):

    @id_auth
    def delete(request, pk, format=None):
        user = request.user
        message = Message.objects.get(pk=pk)
        if (message.sender==user):
            message.delete()
            return HttpResponse(status=201)
        return Response(status=status.HTTP_204_NO_CONTENT)


@method_decorator(csrf_exempt, name='dispatch')
class MessageListView(APIView):

    @id_auth
    def get(request, format=None):
        user = request.user
        messages = Message.objects.filter(sender=user)
        messages |=Message.objects.filter(receiver=user)
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)


@method_decorator(csrf_exempt, name='dispatch')
class LastMessageListView(APIView):

    @id_auth
    def get(request, format=None):
        user = request.user
        rooms = Room.objects.filter(user1=user)
        rooms |= Room.objects.filter(user2=user)
        last_messages = Message.objects.none()

        for room in rooms:
            last_msg = Message.objects.filter(room=room).order_by('-datetime').first()
            last_messages |= Message.objects.filter(pk=last_msg.pk).order_by('-datetime')

        serializer = MessageSerializer(last_messages, many=True)
        return Response(serializer.data)


@method_decorator(csrf_exempt, name='dispatch')
class DetailMessageListView(APIView):
    @id_auth
    def get(request, pk, format=None):
        user = request.user
        room = Room.objects.get(pk=pk)
        if (room.user1==user) or (room.user2==user):
            messages = Message.objects.filter(room=pk).order_by('datetime')
            serializer = MessageSerializer(messages, many=True)
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)


@method_decorator(csrf_exempt, name='dispatch')
class GetOtherUsersPetListView(APIView):

    @id_auth
    def get(request, pk, format=None):
        user = request.user
        room = Room.objects.get(pk=pk)
        if (room.user1 == user):
            other = room.user2
        elif (room.user2 == user):
            other = room.user1
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        pet = Pet.objects.filter(owner=other)
        serializer = PetSerializer(pet, many=True)
        return Response(serializer.data)


@method_decorator(csrf_exempt, name='dispatch')
class RoomInfotView(APIView):

    @id_auth
    def get(request, pk, format=None):
        user = request.user
        room = Room.objects.get(pk=pk)
        if (room.user1==user) or (room.user2==user):
            serializer = RoomSerializer(room)
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)


@method_decorator(csrf_exempt, name='dispatch')
class GetRoomPartnerNicknameView(APIView):

    @id_auth
    def get(request, pk, format=None):
        user = request.user
        room = Room.objects.get(pk=pk)
        if (room.user1==user):
            partner = room.user2
            serializer = UserNicknameSerializer(partner)
        elif (room.user2==user):
            partner = room.user1
            serializer = UserNicknameSerializer(partner)
        else:
            Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data)