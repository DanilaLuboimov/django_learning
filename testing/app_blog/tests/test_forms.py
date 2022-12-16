from django.test import TestCase

from app_blog.forms import AuthForm, RegisterForm, \
    ProfileForm, ArticleForm


class AuthFormTest(TestCase):
    def test_username_label(self):
        form = AuthForm()
        self.assertEqual(form.fields["username"].label, "Логин")

    def test_password_label(self):
        form = AuthForm()
        self.assertEqual(form.fields["password"].label, "Пароль")


class RegisterFormTest(TestCase):
    def test_about_field(self):
        form = RegisterForm()
        self.assertEqual(form.fields["about"].label, "О себе")
        self.assertEqual(form.fields["about"].max_length, 500)


class ProfileFormTest(TestCase):
    def test_firstname_field(self):
        form = ProfileForm()
        self.assertEqual(form.fields["firstname"].label, "Имя")
        self.assertEqual(form.fields["firstname"].max_length, 30)

    def test_lastname_field(self):
        form = ProfileForm()
        self.assertEqual(form.fields["lastname"].label, "Фамилия")
        self.assertEqual(form.fields["lastname"].max_length, 30)

    def test_about_field(self):
        form = ProfileForm()
        self.assertEqual(form.fields["about"].label, "О себе")
        self.assertEqual(form.fields["about"].max_length, 500)

    def test_filling_firstname_and_lastname(self):
        form = ProfileForm(firstname="Name", lastname="Lastname")
        self.assertEqual(form.fields["firstname"].empty_value, "Name")
        self.assertEqual(form.fields["lastname"].empty_value, "Lastname")

    def test_filling_all_information(self):
        form = ProfileForm(firstname="Name", lastname="Lastname", about="About")
        self.assertEqual(form.fields["firstname"].empty_value, "Name")
        self.assertEqual(form.fields["lastname"].empty_value, "Lastname")
        self.assertEqual(form.fields["about"].empty_value, "About")


class ArticleFormTest(TestCase):
    def test_file_field(self):
        form = ArticleForm()
        self.assertEqual(form.fields["file"].label, "Изображения")
