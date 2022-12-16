from django.contrib import admin
from app_shops.models import Shops, Products, Goods


class ShopsAdmin(admin.ModelAdmin):
    list_display = ("name",)


class ProductsAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "code",)


class GoodsAdmin(admin.ModelAdmin):
    list_display = ("product", "store", "price", "remains")


admin.site.register(Shops, ShopsAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(Goods, GoodsAdmin)
