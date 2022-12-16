from django.urls import path
from app_realty.views import RealtyListView, RealtyDetailView

urlpatterns = [
    path("", RealtyListView.as_view(), name="realty_list"),
    path("<int:pk>", RealtyDetailView.as_view(), name="realty_detail"),
]
