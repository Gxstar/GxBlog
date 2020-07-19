"""GxBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include,re_path
from . import views
from blog import views as bg_views

urlpatterns = [
    path('admin1/', admin.site.urls),
    path('admin/', views.admin, name="admin"),
    path('', views.index, name="index"),
    path('blog/', include('blog.urls')),
    path('admin/add/',bg_views.article_add,name="add"),
    path('admin/edit_<int:article_id>/',bg_views.article_edit,name="edit"),
    path('admin/delete_<int:article_id>/',bg_views.article_delete,name="delete"),

    # 正则匹配
    re_path('^admin/add/article_save/$',bg_views.article_save,name="new_save"),
    re_path('^admin/edit_(\d+)/article_save/$',bg_views.article_save,name="save"),
    re_path('^admin/(.+)/$',views.action,name="action")
]
