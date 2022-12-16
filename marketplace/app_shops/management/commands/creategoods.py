from django.core.management import BaseCommand
from app_shops.models import Shops, Products, Goods


class Command(BaseCommand):
    help = 'Создание 10000 пакетов!!!'

    def handle(self, *args, **options):
        shop = Shops.objects.create(name="Пакеты-майки")
        product = Products.objects.create(
            name="Пакет черный",
            code="ПАКЕТ-007"
        )

        for _ in range(10000):
            Goods.objects.create(
                product=product,
                store=shop
            )

        self.stdout.write('База пакетов успешно загружена')
