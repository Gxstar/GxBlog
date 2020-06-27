'''
处理首页功能函数
'''
from bs4 import BeautifulSoup
import requests
from django.shortcuts import render


def index(requests):
    return render(requests, "index.html", get_background())


def get_background():
    '''获得每日bing图片作为首页背景
    输入：无
    返回：dict(图片地址)
    '''
    context = {}
    origin_url = "https://cn.bing.com/HPImageArchive.aspx?idx=0&n=1"
    xml_file = requests.get(origin_url).content
    bs = BeautifulSoup(xml_file, "lxml")
    result_url = "https://cn.bing.com"+bs.url.string
    context['url'] = result_url
    return context


def admin(request):
    """
    跳转后台管理页面
    """
    img_url = get_background()['url']
    if request.user.is_authenticated:
        return render(request, 'admin/admin.html')
    else:
        return render(request, 'admin/log.html', {'err_msg': "", 'img_url': img_url})


def action(request, action):
    if action == "home":
        return render(request, 'admin/home.html', {'param': action})
    elif action == "article":
        return render(request, 'admin/article.html', {'param': action})
    elif action == "category":
        return render(request, 'admin/category.html', {'param': action})
    elif action == "tag":
        return render(request, 'admin/tag.html', {'param': action})
    else:
        return render(request, 'admin/comment.html', {'param': action})
