# 标准库
import string
import random
from datetime import datetime
# 三方库
from django.http.response import JsonResponse
from django.shortcuts import render
from django.core.mail import send_mail
from .models import Captcha
# DIY库
from kk_blog.settings import *


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


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
    send_mail(subject="kk博客注册验证码", message=f"您的注册验证码是：{captcha}", recipient_list=[email], from_email=None)
    return JsonResponse({"code": 200, "message": "邮箱验证码发送成功！"})
