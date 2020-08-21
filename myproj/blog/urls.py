from django.contrib import admin
from django.urls import path, re_path
from .views import ArticleList, ArticleDetail, CategoryList, AuthorList

app_name = 'blog'
urlpatterns = [
    path('', ArticleList.as_view(), name='index'),
    path('p/<int:page>', ArticleList.as_view(), name='index'),
    path('article/<slug:slug>', ArticleDetail.as_view(), name='details'),
    re_path(r'^category/(?P<slugs>[-\w/]*)/p/(?P<page>[0-9]+)/$', CategoryList.as_view(), name='category'),
    re_path(r'^category/(?P<slugs>[-\w/]*)/$', CategoryList.as_view(), name='category'),
    path('author/<slug:username>', AuthorList.as_view(), name='author'),
    path('author/<slug:username>/p/<int:page>', AuthorList.as_view(), name='author'),
]