from django.urls import path
from . import views

app_name = 'blog'  # 指定 app 命名空间

urlpatterns = [
    path('index/', views.index, name='index'),
]
