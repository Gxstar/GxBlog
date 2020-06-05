"""
设置管理页面
"""
from django.contrib import admin
from .models import Category, Tag, Article
# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    """
    文章模型管理
    """
    list_display = ('title', 'createTime', 'updateTime')


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Article, ArticleAdmin)
