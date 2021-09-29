from django.contrib import admin

from .models import Room, Message

# Register your models here.
class RoomAdmin(admin.ModelAdmin):
    list_display = ('user1', 'user2')

admin.site.register(Room, RoomAdmin)


class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'content', 'datetime')

admin.site.register(Message, MessageAdmin)