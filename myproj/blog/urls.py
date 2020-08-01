from django.contrib import admin
from django.urls import path
from .views import index, details, category

app_name = 'blog'
urlpatterns = [
    path('', index, name='index'),
    path('article/<slug:slug>', details, name='details'),
    path('category/<slug:slug>', category, name='category'),
]