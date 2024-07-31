# 三方库
from django.shortcuts import render, reverse, redirect
from django.http.response import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST, require_GET
from .models import BlogCategory, Blog, BlogComment
from .forms import PublishBlogForm
from django.db.models import Q


# 首页的视图函数
def index(request):
    blogs = Blog.objects.all()
    return render(request, "index.html", context={"blogs": blogs})


# 博客详情视图函数
def blog_detail(request, blog_id):
    try:
        # 获取过滤结果的第一条数据
        blog = Blog.objects.get(pk=blog_id)
    except Exception as e:
        blog = None

    return render(request, "blog_detail.html", context={"blog": blog})


# reverse_lazy是整个项目加载完才会加载
# @login_required(login_url=reverse_lazy("kkauth:login")
# @login_required(login_url="/auth/login")
@login_required()
@require_http_methods(["GET", "POST"])
def pub_blog(request):
    """
    @login_required()
    用户认证：确保请求视图的用户已经通过身份验证。
    重定向：如果用户未登录，他们会被重定向到登录页面。默认情况下，重定向的URL是settings.LOGIN_URL中指定的URL。
    灵活性：它允许开发者自定义重定向逻辑，例如，可以指定一个不同的重定向URL，或者在用户登录后返回到他们最初尝试访问的页面。
    """
    if request.method == "GET":
        catagories = BlogCategory.objects.all()
        return render(request, "pub_blog.html", context={"categories": catagories})
    else:
        form = PublishBlogForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            category_id = form.cleaned_data["category"]
            blog = Blog.objects.create(title=title, content=content, category_id=category_id, author=request.user)
            return JsonResponse({"code": 200, "message": "博客发布成功！", "data": {
                "blog_id": blog.id,
            }})
        else:
            print(form.errors)
            return JsonResponse({"code": 400, "message": "参数错误！"})


@require_POST
@login_required()
def pub_comment(request):
    blog_id = request.POST.get("blog_id")
    content = request.POST.get("content")
    BlogComment.objects.create(content=content, author=request.user, blog_id=blog_id)
    # 重定向到博客详情页
    return redirect(reverse('blog:blog_detail', kwargs={'blog_id': blog_id}))


@require_GET
def search(request):
    # /search?q=xxx
    q = request.GET['q']
    # 从博客的标题和内容中查找含有q关键字的博客 F 和 Q表达式 icontains代表忽略大小写
    blogs = Blog.objects.filter(Q(title__icontains=q) | Q(content__icontains=q)).all()
    return render(request, 'index.html', context={"blogs": blogs})
