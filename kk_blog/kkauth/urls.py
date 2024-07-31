from django.urls import path
from . import views

app_name = 'kkauth'

urlpatterns = [
    path('login', views.kk_login, name='login'),
    path('logout', views.kk_logout, name='logout'),
    path('register', views.register, name='register'),
    path('captcha', views.send_email_captcha, name='send_email_captcha'),
]