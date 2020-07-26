from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Article

def index(request):
    context = {
        'articles' : Article.objects.filter(status='p').order_by('-published')
    }
    return render(request, 'blog/index.html', context)

def details(request, slug):
    context = {
        'article' : get_object_or_404(Article, slug=slug, status='p')
    }
    return render(request, 'blog/details.html', context)