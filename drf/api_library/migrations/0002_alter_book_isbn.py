# Generated by Django 4.1 on 2022-11-04 01:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(max_length=13, validators=[django.core.validators.RegexValidator('[0-9-]*')], verbose_name='Книжный номер'),
        ),
    ]
