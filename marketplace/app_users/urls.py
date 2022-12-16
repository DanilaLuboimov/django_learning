from django.urls import path
from .views import AnotherLoginView, AnotherLogoutView, register_view, \
    AccountView, BalanceView

urlpatterns = [
    path("login/", AnotherLoginView.as_view(), name="login"),
    path("logout/", AnotherLogoutView.as_view(), name="logout"),
    path("register/", register_view, name="register"),
    path("account/", AccountView.as_view(), name="account"),
    path("account/balance/", BalanceView.as_view(), name="balance"),
]
