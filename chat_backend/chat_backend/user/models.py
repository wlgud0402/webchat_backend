from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class User(models.Model):
    google_id = models.CharField(
        ("구글로그인 아이디"), max_length=254, null=True, default="default")
    email = models.EmailField(
        ("사용자 이메일"), max_length=254, null=True, default="default@naver.com")
    nickname = models.CharField(("닉네임"), max_length=50)
    peer_id = models.CharField(
        ("피어 id"), max_length=254, null=True, default="default")
    user_type = models.CharField(
        ("유저타입"), max_length=50, null=True, default="GUEST")
    room_id = models.IntegerField(("방번호"), null=True, default=0)
    room_uuid = models.CharField(
        ("방 uuid"), max_length=254, null=True, default="NULL")
    created_at = models.DateTimeField(("가입일"), auto_now_add=True)

    def __str__(self):
        return self.nickname

    class Meta:
        ordering = ['-user_type']
