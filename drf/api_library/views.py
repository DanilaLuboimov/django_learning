from api_library.models import Author, Library
from rest_framework.generics import ListAPIView
from api_library.serializers import AuthorSerializer, \
    LibrarySerializer


class AuthorList(ListAPIView):
    """Представление для получения списка авторов"""
    serializer_class = AuthorSerializer

    def get_queryset(self):
        queryset = Author.objects.all()

        firstname = self.request.query_params.get("firstname")

        if firstname:
            queryset = queryset.filter(firstname=firstname)

        return queryset


class LibraryList(ListAPIView):
    """Представление для получения списка книг с их авторами"""
    serializer_class = LibrarySerializer

    def get_queryset(self):
        queryset = Library.objects.all()

        title = self.request.query_params.get("title")
        author = self.request.query_params.get("author")
        page_count = self.request.query_params.get("page_count")

        if title and author:
            queryset = queryset.filter(book__title=title,
                                       author__lastname=author)
        elif page_count:
            if page_count[0] == "<":
                queryset = queryset.exclude(
                    book__page_count__gte=int(page_count[1::]))
            elif page_count[0] == ">":
                queryset = queryset.exclude(
                    book__page_count__lte=int(page_count[1::]))
            else:
                queryset = queryset.filter(book__page_count=int(page_count))

        return queryset
