from django.shortcuts import render
from .models import Category,Tag,Article
from bs4 import BeautifulSoup
# Create your views here.
def home(request):
    AllCategory=Category.objects.all()
    AllTag=Tag.objects.all()
    context={
        'CategoryList':AllCategory,
        'TagList':AllTag
    }
    PostCount=Article.objects.count()
    PageCount=int(PostCount/5)+1
    context['PostCount']=PostCount
    context['PageCount']=PageCount
    context['PageCountList']=list(range(1,PageCount+1))
    if request.method=='GET':
        page=request.GET.get('page')
        if page==None:
            page=1
        # 判断页码参数是否可以转化为整数
        elif page.isnumeric():
            page=int(page)
        else:
            pass
        ArticleList=Article.objects.all()[(0+5*(page-1)):(4+5*(page-1))]
        # 提取文章前100个字节作为简介
        for index,val in enumerate(ArticleList):
            bs=BeautifulSoup(val.body,"lxml")
            i=bs.get_text().strip()[0:100]
            ArticleList[index].info=i
        # 给需要的参数赋值
        context['ArticleList']=ArticleList
        context['ActivePage']=page
        return render(request,'blog/index.html',context)
    else:
        pass
# 文章展示页面
def showPost(request,article_id):
    AllCategory=Category.objects.all()
    AllTag=Tag.objects.all()
    article=Article.objects.get(id=article_id)
    context={
        'CategoryList':AllCategory,
        'TagList':AllTag,
        'article':article
    }
    return render(request,'blog/post.html',context)
# 分类展示页面
def showCate(request,category_id):
    pass