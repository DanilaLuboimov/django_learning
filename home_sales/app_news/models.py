from django.db import models
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=128, verbose_name="заголовок")
    text = models.TextField(verbose_name="текст")
    date_created = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True,
                                       verbose_name="опубликованная")
    description = models.TextField(verbose_name='описание', default='')
        
    def get_absolute_url(self):
        return reverse('news_detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'новости'
        db_table = 'news'

    def __str__(self):
        return self.title
