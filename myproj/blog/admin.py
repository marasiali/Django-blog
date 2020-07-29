from django.contrib import admin
from .models import Category, Article
from .extensions.utils import convert_to_persian_digits

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position', 'title', 'slug', 'category_article_count', 'status')
    list_filter = ('status',)
    search_fields = ('title', 'slug')
    prepopulated_field = {'slug': ('title',)}

    def category_article_count(self, obj):
        cat_all_articles = Article.objects.filter(category=obj)
        cat_draft_articles = cat_all_articles.filter(status='d')
        output = '{}  ({} پیش‌نویس)'.format(cat_all_articles.count(),
                                          cat_draft_articles.count())
        return convert_to_persian_digits(output)
    category_article_count.short_description = 'تعداد مطالب'


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'jpublished', 'category_to_str', 'status')
    list_filter = ('published', 'status')
    search_fields = ('title', 'description', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['status', '-published']

    def category_to_str(self, obj):
        return ', '.join(map(lambda cat : cat.title, obj.category.all()))
    category_to_str.short_description = 'دسته‌بندی‌ها'
    

admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
