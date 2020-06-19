'''
处理首页功能函数
'''
from bs4 import BeautifulSoup
import requests
from django.shortcuts import render


def index(requests):
    return render(requests, "index.html",get_background())


def get_background():
    '''获得每日bing图片作为首页背景
    输入：无
    返回：dict(图片地址)
    '''
    context = {}
    origin_url="https://cn.bing.com/HPImageArchive.aspx?idx=0&n=1"
    xml_file=requests.get(origin_url).content
    bs=BeautifulSoup(xml_file,"lxml")
    result_url="https://cn.bing.com"+bs.url.string
    context['url']=result_url
    return context
