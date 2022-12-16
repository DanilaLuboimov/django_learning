from django import forms
from django.contrib.auth.models import User
from .models import Article
from django.contrib.auth.forms import AuthenticationForm, UsernameField, \
    UserCreationForm


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
    about = forms.CharField(max_length=500, widget=forms.Textarea,
                            label="О себе")

    class Meta:
        model = User
        fields = (
            'username', 'first_name', 'last_name',
            'password1', 'password2'
        )


class UploadArticleForm(forms.Form):
    file = forms.FileField()


class ProfileForm(forms.Form):
    firstname = forms.CharField(max_length=30, required=False,
                                label="Имя")
    lastname = forms.CharField(max_length=30, required=False,
                               label="Фамилия")
    about = forms.CharField(max_length=500, widget=forms.Textarea,
                            label="О себе", required=False)

    def __init__(self, **kwargs):
        super().__init__(kwargs)
        if len(kwargs) != 0:
            self.fields["firstname"].empty_value = kwargs["firstname"]
            self.fields["lastname"].empty_value = kwargs["lastname"]

            if kwargs.get("about") is None:
                self.fields["about"].empty_value = ""
            else:
                self.fields["about"].empty_value = kwargs["about"]


class ArticleForm(forms.ModelForm):
    file = forms.ImageField(
        required=False,
        label="Изображения",
        widget=forms.ClearableFileInput(
            attrs={"multiple": True}))

    class Meta:
        model = Article
        fields = ("title", "description")
