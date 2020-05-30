from django.shortcuts import render
from .models import Category,Tag,Article
from bs4 import BeautifulSoup

# global variable全局变量
AllCategory=Category.objects.all()
AllTag=Tag.objects.all()
context={
    'CategoryList':AllCategory,
    'TagList':AllTag
}

# Create your views here.
def home(request):
    global context
    PostCount=Article.objects.count()
    PageCount=int(PostCount/5)+1 if PostCount%5!=0 else int(PostCount/5)
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
        ArticleList=Article.objects.all()[(0+5*(page-1)):(5+5*(page-1))]
        # 提取文章前156个字节作为简介
        for index,val in enumerate(ArticleList):
            bs=BeautifulSoup(val.body,"lxml")
            i=bs.get_text().strip()[0:156]
            ArticleList[index].info=i
        # 给需要的参数赋值
        context['ArticleList']=ArticleList
        context['ActivePage']=page
        return render(request,'blog/index.html',context)
    else:
        pass
# 文章展示页面
def showPost(request,article_id):
    global context
    article=Article.objects.get(id=article_id)
    context['article']=article
    return render(request,'blog/post.html',context)
# 分类列表展示页面
def showCate(request,category_id):
    global context
    return render(request,'blog/category.html',context)
# 标签列表展示页面
def showTag(request,tag_id):
    global context
    return render(request,'blog/tag.html',context)