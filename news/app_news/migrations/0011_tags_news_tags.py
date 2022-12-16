# Generated by Django 4.1 on 2022-09-11 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0010_alter_news_create_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название тега')),
            ],
        ),
        migrations.AddField(
            model_name='news',
            name='tags',
            field=models.ManyToManyField(to='app_news.tags'),
        ),
    ]