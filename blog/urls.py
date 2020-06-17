"""
url匹配模块
"""
from django.urls import path, re_path
from django.contrib.auth.views import LogoutView, LoginView
from . import views

urlpatterns = [
    path('', views.home, name='blog_home'),
    re_path(r'^(.*)logout/$', LogoutView.as_view(next_page='/blog/'), name='logout'),
    path('post_<int:article_id>/', views.show_post, name="show_post"),
    path('category_<int:category_id>/', views.show_cate, name="show_cate"),
    path('tag_<int:tag_id>/', views.show_tag, name="show_tag"),
    path('create/', views.create_post, name="create_post"),
    path(r'login/', views.login, name="login")
]
