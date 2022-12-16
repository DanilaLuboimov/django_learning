from rest_framework import serializers
from api_library.models import Author, Book, Library


class AuthorForLibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ("firstname", "lastname")


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("title", "release", "page_count", "isbn")


class LibrarySerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)
    author = AuthorForLibrarySerializer(read_only=True)

    class Meta:
        model = Library
        fields = "__all__"
