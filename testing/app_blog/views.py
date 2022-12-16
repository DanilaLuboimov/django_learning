from django.contrib.auth import authenticate, login
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Profile, Article, File
from .forms import AuthForm, RegisterForm, ProfileForm, ArticleForm, \
    UploadArticleForm
from django.http import HttpResponseRedirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from csv import reader


class MainView(View):
    def get(self, request):
        return render(request, "main.html")

    def post(self, request):
        return self.get(request)


class ArticlesView(ListView):
    model = Article
    template_name = "blog/article_list.html"
    context_object_name = "articles"

    def post(self, request, *args, **kwargs):
        return HttpResponseRedirect("/blog/")


class ArticlesDetailView(DetailView):
    model = Article
    context_object_name = "article"
    template_name = "blog/article_detail.html"

    def get(self, request, *args, **kwargs):
        images = File.objects.filter(article_id=self.kwargs["pk"])

        self.object = self.get_object()
        context = self.get_context_data(object=self.object,
                                        images=images)

        return self.render_to_response(context)


class UploadArticlesView(View):
    def get(self, request):
        upload_file_form = UploadArticleForm()

        return render(request, 'blog/upload_file.html', context={
            'form': upload_file_form
        })

    def post(self, request):
        upload_file_form = UploadArticleForm(request.POST, request.FILES)
        user = User.objects.get(id=request.user.id)

        if upload_file_form.is_valid():
            article_file = upload_file_form.cleaned_data['file'].read()
            article_str = article_file.decode('utf-8').split('\n')
            csv_reader = reader(article_str, delimiter=";", quotechar='"')
            for row in csv_reader:
                if len(row) == 0:
                    continue

                Article.objects.create(
                    title=row[0],
                    description=row[1],
                    author=user
                )

        return HttpResponseRedirect("/")


class ArticleView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            raise PermissionDenied()

        form_article = ArticleForm()
        return render(request, "blog/create_article.html", context={
            "form_article": form_article
        })

    def post(self, request):
        user = User.objects.get(id=request.user.id)
        article_form = ArticleForm(data=request.POST, files=request.FILES)
        if article_form.is_valid():
            article = Article.objects.create(
                title=request.POST.get("title"),
                description=request.POST.get("description"),
                author=user
            )

            files = request.FILES.getlist("file")
            for f in files:
                instance = File(file=f, article=article)
                instance.save()
            return HttpResponseRedirect("/")

        return render(request, "blog/create_article.html", context={
            "form_article": article_form
        })


class EditProfileView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            raise PermissionDenied()

        user = User.objects.get(id=request.user.id)
        try:
            about = Profile.objects.get(user_id=user.id)
        except Exception:
            about = 0

        if about == 0:
            form = ProfileForm(firstname=user.first_name,
                               lastname=user.last_name)
        else:
            form = ProfileForm(firstname=user.first_name,
                               lastname=user.last_name,
                               about=user.profile.about)

        return render(request, "blog/profile.html", context={
            "form": form
        })

    def post(self, request):
        user = User.objects.get(id=request.user.id)
        profile = Profile.objects.get(user_id=user.id)
        form = ProfileForm(data=request.POST)

        if form.is_valid():
            user.first_name = request.POST.get("firstname")
            user.last_name = request.POST.get("lastname")
            profile.about = request.POST.get("about")
            profile.save()
            user.save()
            return HttpResponseRedirect("/blog/profile/")

        return HttpResponseRedirect("/")


class AnotherLoginView(LoginView):
    template_name = "blog/login.html"
    form_class = AuthForm
    next_page = "/"


class AnotherLogoutView(LogoutView):
    next_page = "/"


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            about = form.cleaned_data.get('about')

            Profile.objects.create(user=user, about=about)

            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'blog/register.html', {'form': form})
