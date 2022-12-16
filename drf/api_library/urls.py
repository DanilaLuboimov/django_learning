from django.urls import path
from api_library.views import LibraryList, AuthorList

urlpatterns = [
    path("library/", LibraryList.as_view()),
    path("author/", AuthorList.as_view()),
]
