from django.contrib import admin
from .models import QuantityRoom, SpaceType, Realty


class QuantityRoomAdmin(admin.ModelAdmin):
    list_display = ("id", "quantity",)


class SpaseTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "space_type",)


class RealtyAdmin(admin.ModelAdmin):
    list_display = ("id", "square", "floor", "price_per_metre")


admin.site.register(QuantityRoom, QuantityRoomAdmin)
admin.site.register(SpaceType, SpaseTypeAdmin)
admin.site.register(Realty, RealtyAdmin)
