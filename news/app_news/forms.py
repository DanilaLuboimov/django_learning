from django import forms
from django.contrib.auth.models import User
from .models import News, Comment, Profile
from django.contrib.auth.forms import AuthenticationForm, UsernameField, \
    UserCreationForm


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['username', 'text']


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['create_by', 'title', 'content']

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if "initial" in kwargs:
            self.fields["create_by"].widget = forms.HiddenInput()


class ApprovalNewsForm(forms.ModelForm):

    class Meta:
        model = News
        fields = ["content", "flag_action", "create_by"]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if "initial" in kwargs:
            self.title = kwargs["initial"]["title"]
            self.id = kwargs["initial"]["id"]
            self.text = kwargs["initial"]["content"]
            self.fields["content"].label = kwargs["initial"]["content"]
            self.fields["create_by"].widget = forms.HiddenInput()
            self.fields["flag_action"].label = kwargs["initial"]["create_by"]


class VerfUsersForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["user", "is_verification"]

    def __init__(self, user_id=None, **kwargs):
        super().__init__(**kwargs)
        if user_id:
            self.fields['user'].widget = forms.HiddenInput()
            self.fields["is_verification"].label = User.objects.get(id=user_id).username


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
    first_name = forms.CharField(max_length=30, required=False, label="Имя")
    last_name = forms.CharField(max_length=30, required=False, label="Фамилия")
    city = forms.CharField(max_length=36, required=False, label="Город")
    phone_number = forms.RegexField(
        regex=r'^(\+7|8)\d{10}$',
        error_messages={
            "invalid": "Вы неверно указали номер телефона. Пример +79313332211 или 89313332211"
        },
        help_text="+79313332211 или 89313332211",
        label="Номер телефона")

    class Meta:
        model = User
        fields = (
            'username', 'first_name', 'last_name',
            'password1', 'password2'
        )
