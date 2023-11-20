from django.db import models

# Create your models here.


class Project(models.Model):
    image = models.ImageField(upload_to='project/', null=False)
    title = models.TextField(max_length=20, null=False)
    description = models.TextField(max_length=200, null=True)

    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.pk} : {self.title}'  # f'' : 변수 내용 직접 출력, self => project(모델)
                                            # 몇번 게시판, 그 게시판의 이름