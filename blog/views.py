"""
这是blog应用的视图函数，处理传递到后端的信息
"""
from typing import List

from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from bs4 import BeautifulSoup
from .models import Category, Tag, Article


def common_context() -> dict:
    """
    设置公共变量
    """
    all_category = Category.objects.all()
    all_tag = Tag.objects.all()
    context = {
        'category_list': all_category,
        'tag_list': all_tag,
        'category_id': 0
    }
    return context


def get_page(request, post_list: List) -> dict:
    """
    处理分页获得分页参数
    """
    post_count = len(post_list)
    page_count = int(post_count/5) + \
        1 if post_count % 5 != 0 else int(post_count/5)
    page_count_list = list(range(1, page_count+1))
    if request.method == 'GET':
        page = request.GET.get('page')
        if page is None:
            page = 1
        # 判断页码参数是否可以转化为整数
        elif page.isnumeric():
            page = int(page)
        else:
            pass
        article_list = post_list[(0+5*(page-1)):(5+5*(page-1))]
        # 提取文章前156个字节作为简介
        for index, val in enumerate(article_list):
            bs_doc = BeautifulSoup(val.body, "lxml")
            i = bs_doc.get_text().strip()[0:156]
            article_list[index].info = i
        page_parameter = {
            'post_count': post_count,
            'page_count': page_count,
            'page_count_list': page_count_list,
            'article_list': article_list,
            'active_page': page
        }
        return page_parameter
    return None


def home(request):
    """
    显示主页
    """
    context = common_context()
    post_list = Article.objects.all()
    home_context = get_page(request, post_list)
    merge_context = {**context, **home_context}
    return render(request, 'blog/index.html', merge_context)


def show_post(request, article_id):
    """
    文章展示页面
    """
    context = common_context()
    article = Article.objects.get(id=article_id)
    post_context = {
        'article': article,
        'category_id': article.category.id
    }
    merge_context = {**context, **post_context}
    return render(request, 'blog/post.html', merge_context)


def show_cate(request, category_id):
    """
    分类列表展示页面
    """
    context = common_context()
    post_list = Article.objects.filter(category__id=category_id)
    home_context = get_page(request, post_list)
    merge_context = {**context, **home_context}
    merge_context["category_id"] = category_id
    return render(request, 'blog/index.html', merge_context)


def show_tag(request, tag_id):
    """
    标签列表展示页面
    """
    context = common_context()
    post_list = Article.objects.filter(tag__id=tag_id)
    home_context = get_page(request, post_list)
    merge_context = {**context, **home_context}
    tag_name = Tag.objects.get(id=tag_id)
    merge_context['tag'] = tag_name
    return render(request, 'blog/tag.html', merge_context)


def login(request):
    """
    登录函数
    """
    context = common_context()
    request.session['login_from'] = request.META.get('HTTP_REFERER', '/')
    if request.method == 'GET':
        # 记住来源的url，如果没有则设置为首页('/')
        return HttpResponseRedirect(request.session['login_from'])
    else:
        username = request.POST.get('username')
        pwd = request.POST.get('pwd')
        user = auth.authenticate(username=username, password=pwd)
        if user:
            auth.login(request, user)
            return HttpResponseRedirect(request.session['login_from'])
        else:
            return HttpResponseRedirect(request.session['login_from'])
