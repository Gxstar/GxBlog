from django.shortcuts import render
from .models import Category,Tag,Article
# Create your views here.
def home(request):
    AllCategory=Category.objects.all()
    context={
        'CategoryList':AllCategory
    }
    if request.method=='GET':
        page=request.GET.get('page')
        if page==None:
            page=1
        # 判断页码参数是否可以转化为整数
        elif page.isnumeric():
            page=int(page)
        else:
            pass
        PostCount=Article.objects.count()
        PageCount=int(PostCount/5)
        ArticleList=Article.objects.all()[(0+5*(page-1)):(4+5*(page-1))]
        return render(request,'blog/index.html',context)
    else:
        pass
    