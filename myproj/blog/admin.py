from django.contrib import admin
from .models import Article

class ArticleClass(admin.ModelAdmin):
    list_display = ('title', 'slug', 'published', 'status')
    list_filter = ('published', 'status')
    search_fields = ('title', 'description', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['status', '-published']

admin.site.register(Article, ArticleClass)
