from django.contrib import admin
from app_users.models import User, Status


class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "first_name", "last_name")


class StatusAdmin(admin.ModelAdmin):
    list_display = ("user", "status", "point")


admin.site.register(User, UserAdmin)
admin.site.register(Status, StatusAdmin)
