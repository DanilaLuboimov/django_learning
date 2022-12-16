from django.urls import path
from .views import ProductView, Showcase, Payment, PopularProducts

urlpatterns = [
    path("search/", ProductView.as_view(), name="search"),
    path("search/<int:product_id>", Showcase.as_view()),
    path("basket/", Payment.as_view(), name="basket"),
    path("analytics/", PopularProducts.as_view(), name="analytics"),
]