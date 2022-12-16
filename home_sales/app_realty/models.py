from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError


class SpaceType(models.Model):
    space_type = models.CharField(max_length=1, verbose_name='тип помещения',
                                  choices=(('1', 'Жилое'), ('2', 'Нежилое')),
                                  default='1', unique=True)

    def __str__(self):
        return self.get_space_type_display()

    class Meta:
        verbose_name = 'Тип помещения'
        verbose_name_plural = 'Типы помещений'
        db_table = 'space_type'


class QuantityRoom(models.Model):
    class RoomType(models.TextChoices):
        ONE = '1к', '1-комнатная'
        TWO = '2к', '2-комнатная'
        THREE = '3к', '3-комнатная'
        FOUR = '4к', '4-комнатная'
        FIVE = '5к', '5-комнатная'
        SIX = '6к', '6-комнатная'
        STUDIO = 'С', 'Студия'

    quantity = models.CharField(max_length=2, verbose_name='количество комнат',
                                choices=RoomType.choices, default=RoomType.ONE,
                                unique=True)

    def __str__(self):
        return self.get_quantity_display()

    class Meta:
        verbose_name = 'Количество комнат'
        verbose_name_plural = 'Количество комнат'
        db_table = 'quantity_room'


class Realty(models.Model):
    square = models.FloatField(verbose_name="площадь",
                               validators=(MinValueValidator(limit_value=1,
                                                             message='Помещение не может быть меньше 1 м^2'),))
    max_floor = models.PositiveSmallIntegerField(verbose_name="этажей в доме")
    floor = models.PositiveSmallIntegerField(verbose_name="этаж")
    price_per_metre = models.PositiveIntegerField(verbose_name="цена за метр")
    address = models.CharField(max_length=255, verbose_name="адрес")
    space_type = models.ForeignKey(SpaceType, on_delete=models.CASCADE,
                                   verbose_name="тип помещения",
                                   related_name="space_types")
    quantity_room = models.ForeignKey(QuantityRoom, on_delete=models.CASCADE,
                                      verbose_name="количество комнат",
                                      related_name="quantity_rooms")
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.quantity_room} кв., {self.square} м2, {self.floor}/{self.max_floor} этаж'

    def clean(self):
        if self.floor > self.max_floor:
            raise ValidationError({
                'floor': 'Этаж квартиры не может быть выше максимального этажа в доме'
            }
            )

    class Meta:
        verbose_name = 'Недвижимость'
        verbose_name_plural = 'Недвижимость'
        db_table = 'realty'
