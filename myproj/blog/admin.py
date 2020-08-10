from django.contrib import admin, messages
from django.utils.html import format_html
from .models import Category, Article
from .extensions.utils import convert_to_persian_digits


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position', 'title', 'slug', 'parent', 'category_article_count', 'status')
    list_filter = ('status',)
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    actions = ('make_active', 'make_deactive')

    def category_article_count(self, obj):
        cat_all_articles = Article.objects.filter(category=obj)
        cat_draft_articles = cat_all_articles.filter(status='d')
        cat_all_articles_count = cat_all_articles.count()
        cat_draft_articles_count = cat_draft_articles.count()
        output = str(cat_all_articles_count)
        if cat_draft_articles_count != 0:
            output += f'({cat_draft_articles_count} پیش‌نویس)'
        return convert_to_persian_digits(output)
    category_article_count.short_description = 'تعداد مطالب'

    def make_active(self, request, queryset):
            updated = queryset.update(status=True)
            updated = convert_to_persian_digits(updated)
            msg = f'{updated} دسته بندی فعال شد.'
            self.message_user(request, msg, messages.SUCCESS)
    make_active.short_description = 'فعال کردن'

    def make_deactive(self, request, queryset):
            updated = queryset.update(status=False)
            updated = convert_to_persian_digits(updated)
            msg = f'{updated} دسته بندی غیر‌فعال شد.'
            self.message_user(request, msg, messages.SUCCESS)
    make_deactive.short_description = 'غیر‌فعال کردن'

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'thumbnail_tag', 'jpublished', 'category_to_str', 'status')
    list_filter = ('published', 'status')
    search_fields = ('title', 'description', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('status', '-published')
    actions = ('make_published', 'make_draft')

    def thumbnail_tag(self, obj):
        thumbnail_tag = '<img src={} width=100 style="border-radius: 3px">'
        return format_html(thumbnail_tag, obj.thumbnail.url)
    thumbnail_tag.short_description = 'تصویر اصلی'

    def category_to_str(self, obj):
        return ', '.join(map(lambda cat : cat.title, obj.category.available()))
    category_to_str.short_description = 'دسته‌بندی‌ها'
    
    def make_published(self, request, queryset):
            updated = queryset.update(status='p')
            updated = convert_to_persian_digits(updated)
            msg = f'{updated} مطلب منتشر شد.'
            self.message_user(request, msg, messages.SUCCESS)
    make_published.short_description = 'انتشار'

    def make_draft(self, request, queryset):
            updated = queryset.update(status='d')
            updated = convert_to_persian_digits(updated)
            msg = f'{updated} مطلب پیش‌نویس شد.'
            self.message_user(request, msg, messages.SUCCESS)
    make_draft.short_description = 'پیش‌نویس کردن'

admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
