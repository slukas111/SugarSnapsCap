from django.contrib import admin
from django.urls import path
from .views import contactView, homeView

urlpatterns = [
    path('contact/', contactView, name='contact'),
    path('', homeView, name='success'),
]