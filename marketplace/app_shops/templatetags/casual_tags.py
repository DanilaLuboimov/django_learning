from django.db.models import Sum
from django.template import Library
from app_shops.models import Basket

register = Library()


@register.simple_tag()
def sum_price(user):
    basket = Basket.objects.filter(user=user).aggregate(
        total_price=Sum('product__price'))
    check_sum = basket.get("total_price")
    return check_sum if check_sum else 0
