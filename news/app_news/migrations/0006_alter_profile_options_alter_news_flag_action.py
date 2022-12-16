# Generated by Django 4.1 on 2022-09-09 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0005_news_create_by_profile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'permissions': (), 'verbose_name_plural': 'Профили пользователей'},
        ),
        migrations.AlterField(
            model_name='news',
            name='flag_action',
            field=models.BooleanField(default=0, verbose_name='Активная новость'),
        ),
    ]
