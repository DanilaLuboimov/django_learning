from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class ContactsSitemap(Sitemap):
    changefreq = 'never'

    def items(self):
        return ["contacts"]

    def location(self, item):
        return reverse(item)


class AboutSitemap(Sitemap):
    changefreq = 'yearly'

    def items(self):
        return ["about"]

    def location(self, item):
        return reverse(item)
