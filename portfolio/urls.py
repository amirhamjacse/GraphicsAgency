from django.contrib import admin
from django.urls import path
from portfolio import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]


