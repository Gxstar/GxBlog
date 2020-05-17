from django.urls import path,re_path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.home,name='BlogHome'),
    re_path(r'^(.*)logout/$',LogoutView.as_view(next_page='/blog/'), name='logout'),
]