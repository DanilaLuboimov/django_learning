# Generated by Django 4.1 on 2022-09-02 03:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0003_alter_comment_options_alter_news_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='user_id',
            new_name='user',
        ),
    ]
