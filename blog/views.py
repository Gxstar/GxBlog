from django.shortcuts import render
from .models import Category,Tag,Article
# Create your views here.
def home(request):
    AllArticle=Article.objects.all()
    AllCategory=Category.objects.all()
    context={
        'ArticleList':AllArticle,
        'CategoryList':AllCategory
    }
    if request.method=='GET':
        return render(request,'blog/index.html',context)
    else:
        pass
    