from django.db import models


# Create your models here.
class Captcha(models.Model):
    email = models.EmailField(unique=True)
    captcha = models.CharField(max_length=4)
    creat_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now_add=True)
