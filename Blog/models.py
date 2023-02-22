from django.db import models
from datetime import datetime
from django.utils.timezone import now
from django.contrib.auth.models import User


class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    text = models.TextField(verbose_name="Описание")
    author = models.CharField(max_length=50, verbose_name="Автор")
    slug = models.CharField(max_length=300, verbose_name="Cлаг")
    timeStamp = models.DateTimeField(default=datetime.now(), blank=True, verbose_name="Дата публикации")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"


class BlogComment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField(verbose_name="Комментарии")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Юзеры")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="Пост")
    parent = models.ForeignKey("self", null=True,  on_delete=models.CASCADE, verbose_name="Радитель")
    timeStamp = models.DateTimeField(default=now(), verbose_name="Дата коммента")

    def __str__(self):
        return f"{self.comment[:13]}... by {self.user}"

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

