from django.contrib.auth import authenticate, login
from django.core.exceptions import PermissionDenied, EmptyResultSet
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView
from .models import News, Comment, Profile
from .forms import NewsForm, CommentForm, AuthForm, RegisterForm, \
    VerfUsersForm, ApprovalNewsForm
from django.http import HttpResponseRedirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User, Group


class MainView(View):
    def get(self, request):
        return render(request, "main.html")


class NewsListView(ListView):
    model = News
    template_name = "news/news_list.html"
    context_object_name = "news"
    queryset = News.objects.filter(flag_action=1)

    def post(self, request, *args, **kwargs):
        return HttpResponseRedirect("/news/")


class NewsDetailView(DetailView):
    model = News
    context_object_name = "news"
    template_name = "news/news_detail.html"

    def get(self, request, *args, **kwargs):
        comment_form = CommentForm()

        try:
            comment_list = Comment.objects.filter(news_id=self.kwargs["pk"])
        except Exception:
            pass

        self.object = self.get_object()
        context = self.get_context_data(object=self.object,
                                        comment_list=comment_list,
                                        comment_form=comment_form)

        if request.user.is_authenticated:
            context['user_id'] = User.objects.get(
                username=request.user.username).id

        return self.render_to_response(context)

    def post(self, request, **kwargs):
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            comment_form.cleaned_data['news_id'] = kwargs['pk']

            if request.POST.get('user_id'):
                comment_form.cleaned_data['user_id'] = request.POST['user_id']

            Comment.objects.create(**comment_form.cleaned_data)

        return HttpResponseRedirect(f"/news/{kwargs['pk']}")


class NewsFormView(View):

    def get(self, request):
        if not request.user.has_perm('app_news.can_create_new'):
            raise PermissionDenied()

        news_form = NewsForm(initial={
            "create_by": request.user.profile.id
        })
        return render(request, "news/new.html", context={
            "news_form": news_form
        })

    def post(self, request):
        news_form = NewsForm(data=request.POST)

        if news_form.is_valid():
            News.objects.create(**news_form.cleaned_data)
            return HttpResponseRedirect("/")
        return render(request, "news/new.html", context={
            "news_form": news_form
        })


class NewsEditFormView(View):
    def get(self, request, news_id):
        create_by_id = News.objects.get(id=news_id).create_by

        if not request.user.is_authenticated and \
                request.user.id != create_by_id:
            raise PermissionDenied()

        news = News.objects.get(id=news_id)
        news_form = NewsForm(instance=news)

        return render(request, 'news/edit.html', context={
            'news_form': news_form,
            'id': news_id
        })

    def post(self, request, news_id):
        news = News.objects.get(id=news_id)
        news_form = NewsForm(data=request.POST, instance=news)

        if news_form.is_valid():
            news.save()
            next = request.POST.get('next', f'/news/{news_id}')
            return HttpResponseRedirect(next)

        return render(request, "news/edit.html", context={
            'news_form': news_form,
            'news_id': news_id
        })


class UsersNewsView(ListView):
    model = News

    def get(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.queryset = News.objects.filter(create_by=request.user.profile.id)

        return render(request, "news/news_list.html", context={
            'news': self.queryset,
        })

    def post(self, request, *args, **kwargs):
        return HttpResponseRedirect("/news/")


class ApprovalNewsView(NewsListView, ListView):
    queryset = News.objects.filter(flag_action=0)

    def get(self, request, *args, **kwargs):
        if not request.user.has_perm('app_news.may_allow_publication'):
            raise PermissionDenied()

        news = News.objects.filter(flag_action=0)
        forms = list()

        for n in news:
            forms.append(ApprovalNewsForm(initial={
                "title": n.title,
                "content": n.content,
                "create_by": n.create_by,
                "flag_action": False,
                "id": n.id
            }))

        super().get(request, *args, kwargs)
        return render(request, "news/news_list.html", context={
            "forms": forms
        })

    def post(self, request, **kwargs):
        update_news = News.objects.get(id=request.POST.get("id_news"))
        new_news_form = ApprovalNewsForm(data=request.POST,
                                         instance=update_news)
        if new_news_form.is_valid():
            new_news_form.save()
            user = Profile.objects.get(id=update_news.create_by.id)
            user.counter_news += 1
            user.save()

        return self.get(request, **kwargs)


class UsersList(View):
    def get(self, request):
        if not request.user.has_perm('app_news.can_verify'):
            raise PermissionDenied()

        users = Profile.objects.filter(is_verification=0)
        forms = list()

        for user in users:
            forms.append(VerfUsersForm(user.user.id, initial={
                "user": user.user,
                "is_verification": False,
            }))

        return render(request, "moderators/verf_users.html",
                      context={"forms": forms})

    def post(self, request):
        update_user = Profile.objects.get(user_id=request.POST.get('user'))
        new_users_form = VerfUsersForm(data=request.POST,
                                       instance=update_user)

        if new_users_form.is_valid():
            group = Group.objects.get(name='verified users')

            if group is not None:
                update_user = User.objects.get(id=update_user.user.id)
                update_user.groups.add(group)
                new_users_form.save()
            else:
                raise EmptyResultSet()

        else:
            forms = VerfUsersForm(data=request.POST)

            return render(request, "moderators/verf_users.html",
                          context={"forms": forms})

        return self.get(request)


class AnotherLoginView(LoginView):
    template_name = "users/login.html"
    form_class = AuthForm
    next_page = "/news/"


class AnotherLogoutView(LogoutView):
    next_page = "/news/"


class ProfileView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            raise PermissionDenied()

        user = User.objects.get(id=request.user.id)
        return render(request, "users/profile.html", context={
            "user": user
        })


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            phone_number = form.cleaned_data.get('phone_number')
            city = form.cleaned_data.get('city')
            Profile.objects.create(
                user=user,
                city=city,
                phone_number=phone_number
            )
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/news/')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})
