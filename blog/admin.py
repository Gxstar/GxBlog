from django.contrib import admin
from .models import Category,Tag,Article
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display=('title','createTime','updateTime')

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Article,ArticleAdmin)