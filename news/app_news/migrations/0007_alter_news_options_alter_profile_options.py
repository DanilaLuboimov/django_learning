# Generated by Django 4.1 on 2022-09-09 02:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0006_alter_profile_options_alter_news_flag_action'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-created_at'], 'permissions': (('can_create_new', 'Может создавать новости'), ('may_allow_publication', 'Может разрешить публикацию')), 'verbose_name_plural': 'Новости'},
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'permissions': (('can_verify', 'Может верифицировать'),), 'verbose_name_plural': 'Профили пользователей'},
        ),
    ]
