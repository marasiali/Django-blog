from django.contrib import admin
from django.urls import path
from .views import ArticleList, ArticleDetail, CategoryList

app_name = 'blog'
urlpatterns = [
    path('', ArticleList.as_view(), name='index'),
    path('p/<int:page>', ArticleList.as_view(), name='index'),
    path('article/<slug:slug>', ArticleDetail.as_view(), name='details'),
    path('category/<slug:slug>', CategoryList.as_view(), name='category'),
    path('category/<slug:slug>/p/<int:page>', CategoryList.as_view(), name='category'),
]