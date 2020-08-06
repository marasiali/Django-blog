from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
from django.http import HttpResponse
from .models import Article, Category


class ArticleList(ListView):
    queryset = Article.objects.published()
    paginate_by = 3


class ArticleDetail(DetailView):
    def get_object(self):
        slug = self.kwargs.get('slug')
        article = get_object_or_404(Article.objects.published(), slug=slug)
        return article


class CategoryList(ListView):
    template_name = 'blog/category_list.html'
    paginate_by = 3
    
    def get_queryset(self):
        slug = self.kwargs.get('slug')
        CategoryList.category = get_object_or_404(Category.objects.available(), slug=slug)
        return CategoryList.category.articles.published()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = CategoryList.category
        return context