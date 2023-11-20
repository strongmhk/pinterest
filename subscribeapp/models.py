from django.contrib.auth.models import User
from django.db import models

from projectapp.models import Project


# Create your models here.


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscription')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='subscription')

    class Meta:
        unique_together = ('user', 'project') # user와 project 1쌍이 가지는 subscription(구독정보)은 단 1개이다 -> 하나의 유저가 하나의 프로젝트를 여러 번 구독할 수 없음
