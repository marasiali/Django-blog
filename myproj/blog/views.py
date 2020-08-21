from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
from django.http import HttpResponse, Http404
from django.contrib.auth.models import User
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
        slugs = self.kwargs.get('slugs')
        category_slug, *subcategory_slugs = slugs.split('/')
        CategoryList.category = get_object_or_404(
            Category.objects.available(),
            slug=category_slug,
            parent=None
        )
        for sub_cat in subcategory_slugs:
            CategoryList.category = get_object_or_404(CategoryList.category.children, slug=sub_cat)

        category_children = Category.objects.available_children(CategoryList.category)
        return Article.objects.published().filter(category__in=category_children).distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = CategoryList.category
        return context


class AuthorList(ListView):
    template_name = 'blog/author_list.html'
    paginate_by = 3
    
    def get_queryset(self):
        username = self.kwargs.get('username')
        AuthorList.author = get_object_or_404(User, username=username)
        return AuthorList.author.articles.published()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = AuthorList.author
        return context