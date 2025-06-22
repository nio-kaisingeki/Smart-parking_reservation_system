"""Project URL configuration."""

from django.contrib import admin
from django.urls import path
from reservations import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("api/create-payment-intent/", views.create_payment_intent, name="create-payment-intent"),
    path("admin/dashboard/", views.dashboard, name="dashboard"),
]
