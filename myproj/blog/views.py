from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponse
from .models import Article, Category

def index(request, page=1):
    all_published_articles = Article.objects.published()
    paginator = Paginator(all_published_articles, 3)
    articles = paginator.get_page(page)
    context = {
        'articles' : articles
    }
    return render(request, 'blog/index.html', context)

def details(request, slug):
    context = {
        'article' : get_object_or_404(Article.objects.published(), slug=slug)
    }
    return render(request, 'blog/details.html', context)

def category(request, slug, page=1):
    cat = get_object_or_404(Category.objects.available(), slug=slug)
    all_published_articles = cat.articles.published()
    paginator = Paginator(all_published_articles, 3)
    articles = paginator.get_page(page)
    context = {
        'category' : cat,
        'articles' : articles,
    }
    return render(request, 'blog/category.html', context)