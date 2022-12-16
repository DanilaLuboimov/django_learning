from django.shortcuts import render
from django.views.generic import ListView, DetailView
from app_news.models import News


class NewsListView(ListView):
    model = News
    template_name = "news/news_list.html"
    queryset = News.objects.filter(is_published=1)
    ordering = "-date_created"
    context_object_name = "news"


class NewsDetailView(DetailView):
    model = News
    template_name = "news/news_detail.html"
    context_object_name = "news"
