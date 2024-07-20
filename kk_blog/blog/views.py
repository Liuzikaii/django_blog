from django.shortcuts import render


# 首页的视图函数
def index(request):
    return render(request, "index.html")
