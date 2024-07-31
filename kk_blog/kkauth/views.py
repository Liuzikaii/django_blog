# 标准库
import string
import random
from datetime import datetime
# 三方库
from django.http.response import JsonResponse
from django.shortcuts import render, redirect, reverse
from django.core.mail import send_mail
from django.views.decorators.http import require_http_methods
from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.models import User
# DIY库
from kk_blog.settings import *
from .models import Captcha
from .forms import RegisterForm, LoginForm


User = get_user_model()


@require_http_methods(['GET', 'POST'])
def kk_login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            remember = form.cleaned_data['remember']
            user = User.objects.filter(email=email).first()
            # 验证登录
            if user and user.check_password(password):
                # 登录
                login(request, user)
                # 判断用户是否需要记住我
                if not remember:
                    # 如果没有点击记住我，那么就要设置过期时间为0，即浏览器关闭后就会过期
                    request.session.set_expiry(0)
                # 如果点击了，那么就什么都不做，使用默认的2周的过期时间
                return redirect('/index')
            else:
                print('邮箱或密码错误!')
                form.add_error('email', '邮箱或者密码错误！')
                return render(request, 'login.html', {'form': form})


def kk_logout(request):
    logout(request)
    return redirect('/login')


@require_http_methods(['GET', 'POST'])
def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # 这个方法会将password进行加密后再存储
            User.objects.create_user(username=username, email=email, password=password)
            # 注册成功 重定向到登录界面进行登录
            return redirect(reverse('kkauth:login'))
        else:
            print(form.errors)
            # 重新跳转到登录页面
            # return redirect(reverse('kkauth:register'))
            return render(request, 'register.html', {'form': form})


def send_email_captcha(request):
    # ?email = xxx 获取到其中的email参数 key=value get('key')
    email = request.GET.get('email')
    # 如果没有参数email 则返回
    if not email:
        return JsonResponse({"code": 400, "message": '必须传递邮箱!'})
    # 生成验证码（取四位阿拉伯数字）
    # ["0", "2", "9", "8"]
    captcha = "".join(random.sample(string.digits, 4))
    # 存储到数据库中 邮箱之前已经存在就更新验证码 邮箱之前不存在则新增数据行
    Captcha.objects.update_or_create(email=email, defaults={'captcha': captcha, 'update_time': datetime.now()})
    print(f"验证码为：{captcha}")
    # recipient_list可以发送给多个邮箱
    send_mail(subject="kk博客注册验证码", message=f"您的注册验证码是：{captcha}", recipient_list=[email], from_email=None)
    return JsonResponse({"code": 200, "message": "邮箱验证码发送成功！"})
