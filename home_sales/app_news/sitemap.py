from django.contrib.sitemaps import Sitemap
from app_news.models import News


class NewsSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.9

    def items(self):
        return News.objects.filter(is_published=1)

    def lastmod(self, obj):
        return obj.date_created
