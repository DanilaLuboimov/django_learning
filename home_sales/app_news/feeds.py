from django.contrib.syndication.views import Feed
from django.db.models import QuerySet
from django.urls import reverse
from app_news.models import News


class NewsFeed(Feed):
    title = "Новости"
    link = "/sitenews/"
    description = "Последние новости"

    def items(self):
        return News.objects.order_by("-date_created")[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description

    def item_link(self, item):
        return reverse("news_detail", args=[item.pk])
