from django.contrib import admin
from .models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "is_published")


admin.site.register(News, NewsAdmin)
