from django.urls import path
from .views import home

app_name = 'account'
urlpatterns = [
    path('', home, name='home'),
]