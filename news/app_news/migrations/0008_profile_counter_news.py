# Generated by Django 4.1 on 2022-09-11 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0007_alter_news_options_alter_profile_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='counter_news',
            field=models.IntegerField(blank=True, default=0, verbose_name='Количество опублекованных ноовостей новостей'),
        ),
    ]
