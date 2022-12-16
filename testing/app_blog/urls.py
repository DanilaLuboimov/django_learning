from django.urls import path
from .views import register_view, AnotherLoginView, AnotherLogoutView, \
    EditProfileView, ArticleView, ArticlesView, ArticlesDetailView, \
    UploadArticlesView

urlpatterns = [
    path("register/", register_view, name="register"),
    path("login/", AnotherLoginView.as_view(), name="login"),
    path("logout/", AnotherLogoutView.as_view(), name="logout"),
    path("profile/", EditProfileView.as_view(),
         name="profile"),
    path("create_article/", ArticleView.as_view(), name="create_article"),
    path("", ArticlesView.as_view(), name="articles"),
    path("<int:pk>", ArticlesDetailView.as_view(), name="article"),
    path("upload_csv/", UploadArticlesView.as_view(), name="upload_csv"),
]
