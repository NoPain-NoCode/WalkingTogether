from django.db import models

from user.models import User

# Create your models here.

class Room(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user1', verbose_name='사용자-1')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user2', verbose_name='사용자-2')

    def __str__(self):
        return str(self.pk)

    class Meta:
        db_table = 'message_room'
        verbose_name = '쪽지 방'
        verbose_name_plural = '쪽지 방'

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender', verbose_name='보내는 사람')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver', verbose_name='받는 사람')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name='방 번호')
    content = models.TextField(verbose_name='내용')
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sender.email

    class Meta:
        db_table = 'message'
        verbose_name = '쪽지'
        verbose_name_plural = '쪽지'