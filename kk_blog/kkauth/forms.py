from django import forms
from django.contrib.auth import get_user_model
from .models import Captcha


User = get_user_model()


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=20, min_length=2, error_messages={
        'required': '请传入用户名！',
        'max_length': '用户名长度应为2~20之间！',
        'min_length': '用户名长度应为2~20之间！'
    })

    email = forms.EmailField(min_length=2, error_messages={
        'required': '请传入邮箱！',
        'invalid': '请传入一个正确的邮箱！'
    })

    captcha = forms.CharField(max_length=4, min_length=4)

    password = forms.CharField(min_length=6, max_length=20)

    # 这个函数避免重复的邮箱出现
    def clean_email(self):
        email = self.cleaned_data['email']
        exists = User.objects.filter(email=email).exists()
        if exists:
            raise forms.ValidationError('邮箱已经被注册！')
        return email

    def clean_captcha(self):
        captcha = self.cleaned_data['captcha']
        email = self.cleaned_data['email']

        captcha_model = Captcha.objects.filter(email=email, captcha=captcha).first()
        if not captcha_model:
            raise forms.ValidationError("验证码错误！")
        # 已经验证成功将数据删除
        captcha_model.delete()
        return captcha


class LoginForm(forms.Form):
    email = forms.EmailField(min_length=2, error_messages={
        'required': '请传入邮箱！',
        'invalid': '请传入一个正确的邮箱！'
    })

    password = forms.CharField(min_length=6, max_length=20)

    # required代表可传可不传
    remember = forms.IntegerField(required=False)
