from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class BlogCategory(models.Model):
    name = models.CharField(max_length=200, verbose_name='分类名称')

    # Django自带的管理系统中使用模型中的哪个字段
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '博客分类'
        verbose_name_plural = verbose_name  # 复数


class Blog(models.Model):
    title = models.CharField(max_length=200, verbose_name='标题')
    content = models.TextField(verbose_name='内容')
    publish_time = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    category = models.ForeignKey(BlogCategory, on_delete=models.SET_DEFAULT, default=1, verbose_name='分类')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '博客'
        verbose_name_plural = verbose_name  # 复数
        ordering = ['-publish_time']  # 根据发布的时间倒叙排序


class BlogComment(models.Model):
    content = models.TextField(verbose_name='内容')
    publish_time = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="comments", verbose_name='所属博客')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = '博客评论'
        verbose_name_plural = verbose_name  # 复数
        ordering = ['-publish_time']  # 根据发布的时间倒叙排序
