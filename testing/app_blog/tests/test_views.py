from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from app_blog.models import Article
from app_blog.forms import ArticleForm, UploadArticleForm, \
    ProfileForm, RegisterForm


class SetData(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(username="TestUser")
        cls.auth_user = Client()
        cls.auth_user.force_login(user)

        for num in range(1, 11):
            Article.objects.create(title="Title %s" % num,
                                   description="description %s" % num,
                                   author=user)


class MainPageTest(TestCase):
    def test_view_url_exist(self):
        resp = self.client.get("/")
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template_and_name(self):
        resp = self.client.get(reverse("main"))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "main.html")


class ArticlesListPageTest(SetData):
    def test_view_url_exist(self):
        resp = self.auth_user.get("/blog/")
        self.assertEqual(resp.status_code, 200)

    def test_contains(self):
        resp = self.auth_user.get(reverse("articles"))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "Title 1")
        self.assertContains(resp, "Автор: TestUser")
        self.assertContains(resp, "Title 10")


class ArticlesDetailPageTest(SetData):
    def test_view_url_exist(self):
        for num in range(1, 11):
            resp = self.auth_user.get(reverse("article", kwargs={"pk": num}))
            self.assertEqual(resp.status_code, 200)
            self.assertContains(resp, "Title %s" % num)
            self.assertContains(resp, "TestUser")
            self.assertContains(resp, "description %s" % num)


class UploadArticlePageTest(SetData):
    def test_view_url_exist_and_contex(self):
        resp = self.auth_user.get("/blog/upload_csv/")
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(isinstance(resp.context["form"], UploadArticleForm))

    def test_view_uses_correct_template_and_name(self):
        resp = self.client.get(reverse("upload_csv"))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "blog/upload_file.html")


class CreateArticlePage(SetData):
    def test_view_url_exist_and_context(self):
        resp = self.auth_user.get("/blog/create_article/")
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(isinstance(resp.context["form_article"], ArticleForm))

    def test_view_uses_correct_template_and_name(self):
        resp = self.auth_user.get(reverse("create_article"))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "blog/create_article.html")


class EditProfileTest(SetData):
    def test_view_url_exist_and_context(self):
        resp = self.auth_user.get("/blog/profile/")
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(isinstance(resp.context["form"], ProfileForm))

    def test_view_uses_correct_template_and_name(self):
        resp = self.auth_user.get(reverse("profile"))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "blog/profile.html")


class RegisterViewTest(SetData):
    def test_view_url_exist_and_context(self):
        resp = self.auth_user.get("/blog/register/")
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(isinstance(resp.context["form"], RegisterForm))

    def test_view_uses_correct_template_and_name(self):
        resp = self.auth_user.get(reverse("register"))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "blog/register.html")
