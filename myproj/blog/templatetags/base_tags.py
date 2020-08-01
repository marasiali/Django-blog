from django import template
from ..models import Category

register = template.Library()

@register.simple_tag
def title():
    return 'وبلاگ جنگویی'

@register.simple_tag
def brand_name():
    return 'جنگو وب'

@register.inclusion_tag('blog/partial/category_navbar.html')
def category_navbar():
    return {
        'categories' : Category.objects.available()
    }

@register.inclusion_tag('blog/partial/category_tag.html')
def article_category_tags(article):
    return {
        'categories' : article.category.available()
    }