"""
django模型设置
"""
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Category(models.Model):
    """
    文章分类
    """
    name = models.CharField('分类', max_length=100)
    sort = models.IntegerField('排序', default=1)

    class Meta:
        verbose_name = "博客分类"
        verbose_name_plural = verbose_name
        ordering = ['sort']

    def __str__(self):
        return self.name

class Tag(models.Model):
    """
    标签
    """
    name = models.CharField('文章标签', max_length=100)

    class Meta:
        verbose_name = "文章标签"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Article(models.Model):
    """
    文章
    """
    title = models.CharField('标题', max_length=100)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='用户')
    cover = models.URLField(
        '封面地址', default='https://i.loli.net/2020/04/08/IHWehlbkQ5nxEma.jpg')
    body = RichTextField()
    tag = models.ManyToManyField(Tag, verbose_name='文章标签', blank=True)
    createTime = models.DateTimeField('创建时间', auto_now_add=True)
    updateTime = models.DateTimeField('修改时间', auto_now=True)
    category = models.ForeignKey(
        Category, on_delete=models.DO_NOTHING, verbose_name='分类', blank=True, null=True)

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = verbose_name
        ordering = ('-createTime',)
    def __str__(self):
        return self.title
