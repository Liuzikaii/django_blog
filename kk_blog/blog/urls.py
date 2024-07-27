from django.urls import path
from . import views

app_name = 'blog'  # 指定 app 命名空间

urlpatterns = [
    path('index/', views.index, name='index'),
    path('blog/<int:blog_id>', views.blog_detail, name='blog_detail'),
    path('blog/pub', views.pub_blog, name='pub_blog'),
]
