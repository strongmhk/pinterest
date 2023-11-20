from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile') # request.user.profile.nickname
    image = models.ImageField(upload_to='profile/', null=True) # upload_to : /media/profile/ 에 이미지 저장
    nickname = models.CharField(max_length=20, unique=True, null=True)
    message = models.CharField(max_length=100, null=True)
