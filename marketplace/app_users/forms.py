from django.contrib.auth.forms import AuthenticationForm, UsernameField, \
    UserCreationForm
from django import forms
from app_users.models import User


class AuthForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(attrs={"autofocus": True}),
        label="Логин"
    )
    password = forms.CharField(
        label="Пароль",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password"}),
    )


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'username', 'first_name', 'last_name',
            'password1', 'password2'
        )