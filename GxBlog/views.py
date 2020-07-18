'''
处理首页功能函数
'''
from bs4 import BeautifulSoup
import requests
from django.shortcuts import render, HttpResponseRedirect
from blog import views as bg_vw
from blog.models import Category, Tag, Article


def index(request):
    '''网站首页
    '''
    return render(request, "index.html", get_background())


def get_background():
    '''获得每日bing图片作为首页背景
    输入：无
    返回：dict(图片地址)
    '''
    context = {}
    origin_url = "https://cn.bing.com/HPImageArchive.aspx?idx=0&n=1"
    xml_file = requests.get(origin_url).content
    bs_parse = BeautifulSoup(xml_file, "lxml")
    result_url = "https://cn.bing.com"+bs_parse.url.string
    context['url'] = result_url
    return context


def admin(request):
    """
    跳转后台管理页面
    """
    img_url = get_background()['url']
    if request.user.is_authenticated:
        return HttpResponseRedirect('./home/')
    else:
        return render(request, 'admin/log.html', {'err_msg': "", 'img_url': img_url})


def action(request, admin_fun):
    '''
    后台管理页面的跳转
    '''
    article_list = Article.objects.filter(
        author__username=request.user.username)
    param = {'param': admin_fun}
    # 管理页面主页
    if admin_fun == "home":
        return render(request, 'admin/home.html', param)
    # 文章管理页面
    elif admin_fun == "article":
        page_context = bg_vw.get_page(request, article_list)
        merge_context = {**param, **page_context}
        return render(request, 'admin/article.html', merge_context)
    # 分类管理页面
    elif admin_fun == "category":
        return render(request, 'admin/category.html', param)
    # 标签管理页面
    elif admin_fun == "tag":
        return render(request, 'admin/tag.html', param)
    # 评论管理页面
    else:
        return render(request, 'admin/comment.html', param)
