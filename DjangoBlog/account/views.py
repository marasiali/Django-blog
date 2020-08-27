from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.models import Article
from blog.extensions.utils import convert_to_persian_digits as fa_digit

class ArticleList(LoginRequiredMixin, ListView):
    template_name = 'account/article-list.html'
    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            queryset = Article.objects.all()
            self.published_count = queryset.filter(status='p').count()
            self.draft_count = queryset.filter(status='d').count()
            return queryset
        else:
            queryset = Article.objects.filter(author=user)
            self.published_count = queryset.filter(status='p').count()
            self.draft_count = queryset.filter(status='d').count()
            return queryset.filter(status='d')
    
    def get_context_data(self):
        context = super().get_context_data()
        context['draft_count'] = fa_digit(self.draft_count)
        context['published_count'] = fa_digit(self.published_count)
        # sidebar variables
        context['has_submenu'] = True
        context['active_sidebar_item'] = 'articles'
        context['active_sidebar_subitem'] = 'article-list'
        return context
    