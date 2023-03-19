from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [

    path('home/', views.home),
    path("", views.poject_index, name = "project_index"),
    path("<int:pk>/", views.project_detail, name = "project_detail"),


]