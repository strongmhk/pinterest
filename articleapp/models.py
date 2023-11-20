from django.contrib.auth.models import User
from django.db import models

from projectapp.models import Project


# Create your models here.

class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='article', null=True) # related_name 옵션은 user.article과 같이 역참조가 가능하게 하기 위해서이다
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, related_name='article', null=True)
    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='article/', null=False)
    content = models.TextField(null=True) # 긴 글 일수도 있으므로 Text 필드 사용
    created_at = models.DateField(auto_now_add=True, null=True)