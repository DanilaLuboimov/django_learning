import logging
import datetime as d

from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.core.exceptions import PermissionDenied
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from .forms import AuthForm, RegisterForm
from .models import Status

logger = logging.getLogger(__name__)


def get_time():
    return d.datetime.now(tz=d.timezone(d.timedelta(hours=3))).strftime(
        '%d.%m.%Y %H:%M:%S ')


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()

            Status.objects.create(user=user)
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'user/register.html', {'form': form})


class AnotherLoginView(LoginView):
    template_name = "user/login.html"
    form_class = AuthForm
    next_page = "/"

    def get_default_redirect_url(self):
        logger.info(
            f"{get_time()} Пользователь под логином {self.request.user.username} вошел в систему")
        return super().get_default_redirect_url()


class AnotherLogoutView(LogoutView):
    next_page = "/"


class MainMenu(View):
    def get(self, request):
        return render(request, "mainmenu.html")

    def post(self, request):
        return self.get(request)


class AccountView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            raise PermissionDenied()

        status = Status.objects.get(user=request.user)
        return render(request, "user/account.html", context={
            "username": request.user.username,
            "firstname": request.user.first_name,
            "lastname": request.user.last_name,
            "status": status,
            "balance": request.user.balance
        })


class BalanceView(View):
    def get(self, request):
        return render(request, "user/balance.html")

    @transaction.atomic
    def post(self, request):
        try:
            if int(request.POST.get("money")) <= 0:
                raise ValueError
            request.user.balance += int(request.POST.get("money"))
            request.user.save()
        except ValueError:
            return HttpResponse(
                content="Пополнить баланс можно только циферками больше нуля",
                status=200)
        else:
            logger.info(
                f'{get_time()} Пользователь {request.user.username} пополнил свой баланс на {request.POST.get("money")}')
        return redirect("account")
