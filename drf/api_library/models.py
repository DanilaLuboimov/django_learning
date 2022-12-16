from django.db import models
from django.core.validators import RegexValidator, MinValueValidator, \
    MaxValueValidator


class Author(models.Model):
    """Модель с авторами книг"""
    firstname = models.CharField(max_length=100, verbose_name="Имя")
    lastname = models.CharField(max_length=100, verbose_name="Фамилия")
    birthdate = models.IntegerField(verbose_name="Дата рождения",
                                    validators=[MinValueValidator(1550),
                                                MaxValueValidator(4000)]
                                    )

    class Meta:
        verbose_name_plural = "Авторы"
        db_table = "authors"

    def __str__(self):
        return f"{self.lastname} {self.firstname}"


class Book(models.Model):
    """Модель с книгами"""
    title = models.CharField(max_length=200, verbose_name="Название")
    isbn = models.CharField(max_length=20, verbose_name="Книжный номер",
                            validators=[RegexValidator(r"^[0-9-]*$")])
    release = models.IntegerField(verbose_name="Год выпуска",
                                  validators=[MinValueValidator(1600),
                                              MaxValueValidator(4000)])
    page_count = models.IntegerField(verbose_name="Количество страниц",
                                     validators=[MinValueValidator(0)])
    author = models.ManyToManyField(Author, through="Library")

    class Meta:
        verbose_name_plural = "Книги"
        db_table = "books"

    def __str__(self):
        return f"{self.title}"


class Library(models.Model):
    """Модель библиотеки объединяющая авторов с их книгами"""
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Библиотека"
        db_table = "library"

    def __str__(self):
        return f"{self.book.title} {self.author.lastname}"
