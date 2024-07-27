from django.urls import path
from . import views

app_name = 'kkauth'

urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
]