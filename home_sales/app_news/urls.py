from django.urls import path
from app_news.views import NewsListView, NewsDetailView
from app_news.feeds import NewsFeed

urlpatterns = [
    path("", NewsListView.as_view(), name="news_list"),
    path("<int:pk>", NewsDetailView.as_view(), name="news_detail"),
    path("feed/", NewsFeed()),
]
