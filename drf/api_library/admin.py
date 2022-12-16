from django.contrib import admin
from api_library.models import Book, Author, Library


class AuthorAdmin(admin.ModelAdmin):
    list_display = ["id", "lastname"]


class BookAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "isbn"]


class LibraryAdmin(admin.ModelAdmin):
    list_display = ["id", "book", "author"]


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Library, LibraryAdmin)
