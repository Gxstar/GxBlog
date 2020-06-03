from django.shortcuts import render
from .models import Category,Tag,Article
from bs4 import BeautifulSoup
from typing import List

# global variable全局变量
AllCategory=Category.objects.all()
AllTag=Tag.objects.all()
context={
    'CategoryList':AllCategory,
    'TagList':AllTag,
    'CategoryId':0
}
# 处理分页获得分页参数
def getPage(request,PostList : List) -> dict: 
    PostCount=len(PostList)
    PageCount=int(PostCount/5)+1 if PostCount%5!=0 else int(PostCount/5)
    PageCountList=list(range(1,PageCount+1))
    if request.method=='GET':
        page=request.GET.get('page')
        if page==None:
            page=1
        # 判断页码参数是否可以转化为整数
        elif page.isnumeric():
            page=int(page)
        else:
            pass
        ArticleList=PostList[(0+5*(page-1)):(5+5*(page-1))]
        # 提取文章前156个字节作为简介
        for index,val in enumerate(ArticleList):
            bs=BeautifulSoup(val.body,"lxml")
            i=bs.get_text().strip()[0:156]
            ArticleList[index].info=i
        PageParameter={'PostCount':PostCount,'PageCount':PageCount,'PageCountList':PageCountList,'ArticleList':ArticleList,'ActivePage':page}
        return PageParameter
    else:
        return {}
# Create your views here.
def home(request):
    global context
    PostList=Article.objects.all()
    HomeContext=getPage(request,PostList)
    MergeContext={**context,**HomeContext}
    return render(request,'blog/index.html',MergeContext)
# 文章展示页面
def showPost(request,article_id):
    global context
    article=Article.objects.get(id=article_id)
    PostContext={
        'article':article,
        'CategoryId':article.category.id
    }
    MergeContext={**context,**PostContext}
    return render(request,'blog/post.html',MergeContext)
# 分类列表展示页面
def showCate(request,category_id):
    global context
    PostList=Article.objects.filter(category__id=category_id)
    HomeContext=getPage(request,PostList)
    MergeContext={**context,**HomeContext}
    MergeContext["CategoryId"]=category_id
    return render(request,'blog/index.html',MergeContext)
# 标签列表展示页面
def showTag(request,tag_id):
    global context
    PostList=Article.objects.filter(tag__id=tag_id)
    HomeContext=getPage(request,PostList)
    MergeContext={**context,**HomeContext}
    return render(request,'blog/tag.html',MergeContext)