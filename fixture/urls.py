from django.contrib import admin
from django.urls import path, include
from .views import indexView, contactView

urlpatterns = [
    path('', indexView, name="index"),
    path('contact/', contactView, name="contact")
]
