from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {
        'posts' : [
            {
                'title' : 'First',
                'desc' : 'I am first',
                'number' : 1
            },
            {
                'title' : 'Second',
                'desc' : 'I am second',
                'number' : 2
            },
            {
                'title' : 'Third',
                'desc' : 'I am third',
                'number' : 3
            },
        ]
    }
    return render(request, 'index.html', context)