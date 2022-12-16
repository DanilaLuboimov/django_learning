from django.core.validators import MinValueValidator
from django.db import models
from app_users.models import User


class Shops(models.Model):
    name = models.CharField(max_length=50, verbose_name="магазин")

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = "Магазины"
        db_table = "shops"


class Products(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    store = models.ManyToManyField(Shops, through="Goods")
    code = models.CharField(max_length=100, verbose_name="код")

    class Meta:
        verbose_name_plural = "Продукция"
        db_table = "products"

    def __str__(self):
        return self.name


class Goods(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    store = models.ForeignKey(Shops, on_delete=models.CASCADE)
    price = models.FloatField(default=100, verbose_name="цена",
                              validators=[
                                  MinValueValidator(0)
                              ])
    remains = models.IntegerField(default=10, verbose_name="остаток",
                                  validators=[
                                      MinValueValidator(0)
                                  ])

    def __str__(self):
        return str(self.product.name)

    class Meta:
        verbose_name_plural = "Товары"
        db_table = "goods"


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             verbose_name="пользователь")
    product = models.ForeignKey(Goods, on_delete=models.CASCADE,
                                verbose_name="товар")

    class Meta:
        verbose_name_plural = "Корзина"
        db_table = "basket"


class History(models.Model):
    product = models.ForeignKey(Goods, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True,
                                verbose_name="Date")

    class Meta:
        verbose_name_plural = "History"
        db_table = "history"
