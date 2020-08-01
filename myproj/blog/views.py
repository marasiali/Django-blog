from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Article, Category

def index(request):
    context = {
        'articles' : Article.objects.published()
    }
    return render(request, 'blog/index.html', context)

def details(request, slug):
    context = {
        'article' : get_object_or_404(Article.objects.published(), slug=slug)
    }
    return render(request, 'blog/details.html', context)

def category(request, slug):
    context = {
        'category' : get_object_or_404(Category.objects.available(), slug=slug)
    }
    return render(request, 'blog/category.html', context)