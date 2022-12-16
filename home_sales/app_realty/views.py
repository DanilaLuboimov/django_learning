from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from app_realty.models import Realty


class About(View):
    def get(self, request):
        return render(request, "main/about.html")


class Main(View):
    def get(self, request):
        return render(request, "main/main.html")


class Contacts(View):
    def get(self, request):
        return render(request, "main/contacts.html")


class RealtyListView(ListView):
    model = Realty
    context_object_name = "realty"
    template_name = "realty/realty_list.html"
    paginate_by = 5
    queryset = Realty.objects.select_related("quantity_room").filter(is_published=1)


class RealtyDetailView(DetailView):
    model = Realty
    context_object_name = "realty"
    template_name = "realty/realty_detail.html"
    queryset = Realty.objects.select_related("space_type", "quantity_room")
