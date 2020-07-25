from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

def index(request):
    context = {
        'articles' : Article.objects.filter(status='p').order_by('-published')
    }
    return render(request, 'blog/index.html', context)

def details(request, slug):
    context = {
        'article' : Article.objects.get(slug=slug, status='p')
    }
    return render(request, 'blog/details.html', context)