from django.shortcuts import render


# 首页的视图函数
def index(request):
    return render(request, "index.html")


# 博客详情视图函数
def blog_detail(request, blog_id):
    return render(request, "blog_detail.html")


def pub_blog(request):
    return render(request, "pub_blog.html")
