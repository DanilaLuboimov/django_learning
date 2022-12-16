from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _
from django.db import models


class User(AbstractUser):
    first_name = models.CharField(_("first name"), max_length=150)
    last_name = models.CharField(_("last name"), max_length=150)
    balance = models.IntegerField(default=10000, verbose_name="balance",
                                  validators=[
                                      MinValueValidator(0)
                                  ])

    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"
        verbose_name_plural = "Пользователи"
        db_table = "users"


class Status(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                verbose_name="пользователь")
    status = models.IntegerField(default=0, choices=[(0, "Новичок"),
                                                     (1, "Опытный покупатель"),
                                                     (2, "Шопоголик")])
    point = models.IntegerField(default=0, verbose_name="point",
                                validators=[
                                    MinValueValidator(0)
                                ])

    def __str__(self):
        user = User.objects.get(id=self.user.id).username
        return f"{user} {self.status}"

    class Meta:
        verbose_name_plural = "Статусы"
        db_table = "status"
