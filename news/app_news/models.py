from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=36, blank=True, verbose_name="Город")
    phone_number = models.CharField(max_length=12, blank=True,
                                    verbose_name="Номер телефона")
    is_verification = models.BooleanField(default=0,
                                          verbose_name="Верифицированный")
    counter_news = models.IntegerField(default=0, blank=True,
                                       verbose_name="Количество опублекованных ноовостей новостей")

    def __str__(self):
        user = User.objects.get(id=self.user.id)
        return user.username

    class Meta:
        verbose_name_plural = "Профили пользователей"
        db_table = "profile"
        permissions = (
            ("can_verify", "Может верифицировать"),
        )


class News(models.Model):
    title = models.CharField(max_length=200, default="Новость",
                             verbose_name="Заголовок новости")
    content = models.TextField(max_length=3000, default="",
                               verbose_name="Текст новости")
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name="Дата создания")
    update_at = models.DateTimeField(auto_now=True,
                                     verbose_name="Дата последнего обновления")
    flag_action = models.BooleanField(default=0, null=False,
                                      verbose_name="Активная новость")
    create_by = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Новости"
        db_table = "news"
        ordering = ["-created_at"]
        permissions = (
            ("can_create_new", "Может создавать новости"),
            ("may_allow_publication", "Может разрешить публикацию"),
        )


class Comment(models.Model):
    username = models.CharField(max_length=20, verbose_name="Ваше имя")
    text = models.CharField(max_length=200, verbose_name="Комментарий")
    news = models.ForeignKey("News", on_delete=models.CASCADE,
                             related_name="news", null=True)
    user = models.ForeignKey("auth.user", on_delete=models.CASCADE,
                             default=None, null=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = 'Комментарии'
        db_table = "comments"
