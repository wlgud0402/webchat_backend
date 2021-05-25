import redis
import redis_server
import json
from django.shortcuts import render, HttpResponse
from .models import Room
from util.scheduler import roomScheduler
from rest_framework import status
from rest_framework.response import Response


def message(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        message = json.loads(data)['message']
        nickname = json.loads(data)['nickname']
        room_id = json.loads(data)['room_id']
        peer_id = json.loads(data)['peer_id']

        r = redis.Redis(host='localhost', port=6379, db=0)

        r.publish('my-chat', json.dumps({
            'room_id': room_id,
            "nickname": nickname,
            "message": message,
            "peer_id": peer_id
        }))

        return Response({"msg": "처리가 완료되었습니다."}, status=status.HTTP_200_OK)
    else:
        return Response({"msg": "잘못된 요청입니다"}, status=status.HTTP_400_BAD_REQUEST)


def changeroomstatus(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        room_id = json.loads(data)['room_id']
        room = Room.objects.get(id=room_id)

        if room.status == 'CLEANING':
            room.status = 'ACTIVE'
            room.save()

            # socket 서버에 퍼블리시를 통해 알려준다
            r = redis.Redis(host='localhost', port=6379, db=0)
            r.publish('room-refresh', json.dumps({
                'room_id': json.loads(data)['room_id'],
            }))
            # 클리닝 돌리고있는 스케쥴러 켄슬시킴
            roomScheduler.cancelRemove(room_id)

        return Response({"msg": "처리가 완료되었습니다."}, status=status.HTTP_200_OK)
    else:
        return Response({"msg": "잘못된 요청입니다"}, status=status.HTTP_400_BAD_REQUEST)
