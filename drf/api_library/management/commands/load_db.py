from django.core.management import BaseCommand
from api_library.models import Author, Book, Library


class Command(BaseCommand):
    help = 'Загрузка базы дынных'

    def handle(self, *args, **options):
        a1 = Author.objects.create(firstname="Александр", lastname="Пушкин", birthdate=1799)
        a2 = Author.objects.create(firstname="Михаил", lastname="Зощенко", birthdate=1894)
        a3 = Author.objects.create(firstname="Самуил", lastname="Маршак", birthdate=1887)
        a4 = Author.objects.create(firstname="Николай", lastname="Гоголь", birthdate=1809)
        a5 = Author.objects.create(firstname="Джек", lastname="Лондон", birthdate=1876)

        b1 = Book.objects.create(title="Руслан и Людмила", release=2008, page_count=175, isbn="978-5-17-016451-6")
        b2 = Book.objects.create(title="Сказка о золотом петушке", release=2004, page_count=16, isbn="5-8029-0481")
        b3 = Book.objects.create(title="Капитанская дочка", release=2006, page_count=207, isbn="5-94563-876-5")
        b4 = Book.objects.create(title="Великие путешественники", release=2006, page_count=62, isbn="5-479-00398-4")
        b5 = Book.objects.create(title="Сказка о глупом мышонке", release=1999, page_count=10, isbn="5-237-04297")
        b6 = Book.objects.create(title="Сказка об умном мышонке", release=2003, page_count=9, isbn="5-17-004370-8")
        b7 = Book.objects.create(title="Мертвые души", release=2004, page_count=491, isbn="978-5-17-008751-8")
        b8 = Book.objects.create(title="Шинель", release=2006, page_count=255, isbn="5-8475-0365-2")
        b9 = Book.objects.create(title="Тарас Бульба", release=2006, page_count=188, isbn="5-08-003948-5")
        b10 = Book.objects.create(title="Странник по звездам", release=2021, page_count=384, isbn="978-5-17-103720-8")

        Library.objects.create(author=a1, book=b1)
        Library.objects.create(author=a1, book=b2)
        Library.objects.create(author=a1, book=b3)
        Library.objects.create(author=a2, book=b4)
        Library.objects.create(author=a3, book=b5)
        Library.objects.create(author=a3, book=b6)
        Library.objects.create(author=a4, book=b7)
        Library.objects.create(author=a4, book=b8)
        Library.objects.create(author=a4, book=b9)
        Library.objects.create(author=a5, book=b10)

        self.stdout.write('База успешно загружена')
