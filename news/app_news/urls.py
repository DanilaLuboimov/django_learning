from django.urls import path
from .views import NewsListView, NewsFormView, NewsDetailView, \
    NewsEditFormView, AnotherLoginView, AnotherLogoutView, register_view, \
    MainView, ProfileView, UsersList, UsersNewsView, ApprovalNewsView

urlpatterns = [
    path('', MainView.as_view(), name="main"),
    path("login/", AnotherLoginView.as_view(), name="login"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("news/", NewsListView.as_view(), name="news_list"),
    path("news/<int:pk>", NewsDetailView.as_view()),
    path("news/new/", NewsFormView.as_view(), name="new_news"),
    path("news/<int:news_id>/edit", NewsEditFormView.as_view(),
         name="edit_news"),
    path("logout/", AnotherLogoutView.as_view(), name="logout"),
    path("register/", register_view, name="register"),
    path("new_users/", UsersList.as_view(), name="new_users"),
    path("my_news/", UsersNewsView.as_view(), name="my_news"),
    path("news_moderation/", ApprovalNewsView.as_view(), name="news_moderation"),
]
