import shutil
import tempfile

from django.test import TestCase, override_settings
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.conf import settings

from app_blog.models import Profile, Article, File


class TestSettings(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(username="TestUser", password="123")
        Profile.objects.create(user=user, about="TestText")
        Article.objects.create(title="TestTitle",
                                         description="TestDescription",
                                         author=user)


class ProfileModelTest(TestSettings):
    def test_user_field(self):
        profile_user = Profile.objects.get(id=1)
        self.assertEqual(profile_user.user.username, "TestUser")

    def test_about_verbose_name(self):
        profile_user = Profile.objects.get(id=1)
        label = profile_user._meta.get_field("about").verbose_name
        self.assertEqual(label, "О себе")

    def test_about_max_length(self):
        profile_user = Profile.objects.get(id=1)
        max_length = profile_user._meta.get_field("about").max_length
        self.assertEqual(max_length, 500)

    def test_vision(self):
        profile_user = Profile.objects.get(id=1)
        self.assertEqual(str(profile_user), "TestUser")


class ArticleModelTest(TestSettings):
    def test_title_verbose_name(self):
        article = Article.objects.get(id=1)
        label = article._meta.get_field("title").verbose_name
        self.assertEqual(label, "Название блога")

    def test_description_verbose_name(self):
        article = Article.objects.get(id=1)
        label = article._meta.get_field("description").verbose_name
        self.assertEqual(label, "Текст блога")

    def test_created_at_verbose_name(self):
        article = Article.objects.get(id=1)
        label = article._meta.get_field("created_at").verbose_name
        self.assertEqual(label, "Дата создания")

    def test_author_verbose_name(self):
        article = Article.objects.get(id=1)
        label = article._meta.get_field("author").verbose_name
        self.assertEqual(label, "Автор")

    def test_title_max_length(self):
        article = Article.objects.get(id=1)
        max_length = article._meta.get_field("title").max_length
        self.assertEqual(max_length, 150)

    def test_author_field(self):
        article = Article.objects.get(id=1)
        self.assertEqual(article.author.username, "TestUser")

    def test_vision(self):
        article = Article.objects.get(id=1)
        self.assertEqual(str(article), "TestTitle TestUser")


@override_settings(MEDIA_ROOT=tempfile.mkdtemp(dir=settings.BASE_DIR))
class FileModelTest(TestSettings):
    def test_file(self):
        small_gif = (
            b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9\x04'
            b'\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02'
            b'\x02\x4c\x01\x00\x3b'
        )
        uploaded = SimpleUploadedFile('small.gif', small_gif,
                                      content_type='image/gif')
        article = Article.objects.get(id=1)
        file = File.objects.create(file=uploaded, article=article)
        verbose_name = file._meta.get_field("file").verbose_name
        self.assertEqual(verbose_name, "Изображения")
        self.assertEqual(file.article, article)

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(settings.MEDIA_ROOT, ignore_errors=True)
        super().tearDownClass()