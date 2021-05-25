from django.urls import path
from .views import index, message, getMessage, changeroomstatus
from .api import RoomAPI, GetRoomAPI, RoomPasswordAPI
from rest_framework import generics


urlpatterns = [
    path('', index, name='home'),
    path('room/', RoomAPI.as_view(), name='room'),
    path('getroom/', GetRoomAPI.as_view(), name='get_room_by_uuid'),
    path('getmessage/', message, name='message'),
    path('changeroomstatus/', changeroomstatus, name='change_room_status'),
    path('roompassword/', RoomPasswordAPI.as_view(), name='roompassword'),
]
