from django.urls import path
from .views import ArticleList, ArticleCreate

app_name = 'account'
urlpatterns = [
    path('', ArticleList.as_view(), name='article-list'),
    path('article/create', ArticleCreate.as_view(), name='article-create'),
]