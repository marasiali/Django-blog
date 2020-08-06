from django.contrib import admin
from django.urls import path
from .views import ArticleList, ArticleDetail, category

app_name = 'blog'
urlpatterns = [
    path('', ArticleList.as_view(), name='index'),
    path('p/<int:page>', ArticleList.as_view(), name='index'),
    path('article/<slug:slug>', ArticleDetail.as_view(), name='details'),
    path('category/<slug:slug>', category, name='category'),
    path('category/<slug:slug>/p/<int:page>', category, name='category'),
]