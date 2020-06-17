'''
处理首页功能函数
'''
from django.shortcuts import render

def index(requests):
    return render(requests,"index.html")