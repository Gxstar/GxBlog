from django.urls import path,re_path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.home,name='blogHome'),
    re_path(r'^(.*)logout/$',LogoutView.as_view(next_page='/blog/'), name='logout'),
    path('post_<int:article_id>/',views.showPost,name="showPost"),
    path('category_<int:category_id>',views.showCate,name="showCate"),
    path('tag_<int:tag_id>',views.showTag,name="showTag"),
]