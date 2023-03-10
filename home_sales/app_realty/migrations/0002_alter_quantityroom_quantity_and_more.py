# Generated by Django 4.1 on 2022-12-08 03:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_realty', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quantityroom',
            name='quantity',
            field=models.CharField(choices=[('1к', '1-комнатная'), ('2к', '2-комнатная'), ('3к', '3-комнатная'), ('4к', '4-комнатная'), ('5к', '5-комнатная'), ('6к', '6-комнатная'), ('С', 'Студия')], default='1к', max_length=2, unique=True, verbose_name='количество комнат'),
        ),
        migrations.AlterField(
            model_name='realty',
            name='quantity_room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quantity_rooms', to='app_realty.quantityroom', verbose_name='количество комнат'),
        ),
        migrations.AlterField(
            model_name='realty',
            name='space_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='space_types', to='app_realty.spacetype', verbose_name='тип помещения'),
        ),
    ]
