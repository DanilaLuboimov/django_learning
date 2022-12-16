from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.TextField(blank=False, max_length=500,
                             verbose_name="О себе")

    def __str__(self):
        user = User.objects.get(id=self.user.id)
        return user.username

    class Meta:
        verbose_name_plural = "Профили пользователей"
        db_table = "profile"


class Article(models.Model):
    title = models.CharField(max_length=150,
                             verbose_name="Название блога")
    description = models.TextField(verbose_name="Текст блога")
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name="Дата создания")
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               verbose_name="Автор")

    def __str__(self):
        vision = str(self.title), str(self.author)
        return " ".join(vision)

    class Meta:
        verbose_name_plural = "Блоги"
        db_table = "article"
        ordering = ["-created_at"]


class File(models.Model):
    file = models.FileField(upload_to='files/', verbose_name="Изображения")
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
