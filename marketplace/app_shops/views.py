import datetime as d
import logging

from django.shortcuts import render, redirect
from django.views import View
from django.db import transaction
from django.db.models import Count

from .models import Products, Goods, Basket, History
from app_users.models import Status
from app_users.views import get_time, logger


class ProductView(View):
    def get(self, request):
        products = Products.objects.all().values("id", "name")
        return render(request, "shop/search.html", context={
            'products': products
        })


class Showcase(View):
    def get(self, request, product_id):
        goods = Goods.objects.select_related('product').prefetch_related(
            'store').filter(product__id=product_id)
        return render(request, "shop/showcase.html", context={
            "goods": goods
        })

    @transaction.atomic
    def post(self, request, product_id):
        product = Goods.objects.get(id=request.POST.get("product_id"))
        Basket.objects.create(user=request.user, product=product)

        product.remains -= 1
        product.save()

        logger.info(
            f"{get_time()} Пользователь {request.user.username} зарезервировал {product.product.code}")
        return self.get(request, product_id)


class Payment(View):
    def get(self, request):
        basket = Basket.objects.select_related('product').filter(
            user=request.user)
        return render(request, "shop/basket.html", context={
            "products": basket
        })

    @transaction.atomic
    def post(self, request):
        basket = Basket.objects.select_related('product').filter(
            user=request.user)
        user = request.user
        status = Status.objects.get(user=user)

        b_sum = 0

        for b in basket:
            History.objects.create(product=b.product)
            b.delete()
            user.balance -= b.product.price
            status.point += b.product.price
            b_sum += b.product.price

        logger.info(
            f'{get_time()} У пользователя {user.username} списано {b_sum} c баланса')

        if status.point >= 5000:
            status.status = 2
            logger.info(
                f'{get_time()} Пользователь {user.username} получил 3 уровень статуса ')
        elif status.point >= 2000:
            status.status = 1
            logger.info(
                f'{get_time()} Пользователь {user.username} получил 2 уровень статуса ')

        status.save()
        user.save()
        return redirect("main")


class PopularProducts(View):
    def get(self, request):
        history = Goods.objects.filter(
            history__date__gt=d.datetime.today() - d.timedelta(
                days=1)).annotate(
            quantity=Count('history')).order_by('-quantity')

        return render(request, "shop/analytics.html", context={
            "first_place": history[0] if len(history) >= 1 else None,
            "second_place": history[1] if len(history) >= 2 else None,
            "third_place": history[2] if len(history) >= 3 else None
        })
