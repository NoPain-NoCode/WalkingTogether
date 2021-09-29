from django.urls import path
from .views import SendMessageView, DeleteMessageView, MessageListView, LastMessageListView, DetailMessageListView, GetOtherUsersPetListView, RoomInfotView, GetRoomPartnerNicknameView

app_name = 'message'

urlpatterns = [
    path('send/', SendMessageView.as_view(), name='send_message'),
    path('delete/<int:pk>/', DeleteMessageView.as_view(), name='delete_message'),
    path('list/', MessageListView.as_view(), name='message_list'),
    path('list/last/', LastMessageListView.as_view(), name='last_message_list'),
    path('list/detail/<int:pk>/', DetailMessageListView.as_view(), name='detail_message_list'),
    path('list/detail/<int:pk>/otheruser/petinfo/', GetOtherUsersPetListView.as_view(), name='get_room_otheruser_pet_list'),
    path('room/<int:pk>/info/', RoomInfotView.as_view(), name='room_info'),
    path('room/<int:pk>/partner/nickname/', GetRoomPartnerNicknameView.as_view(), name='get_room_partner_nickname')
]