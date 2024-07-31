from django.contrib import admin
from .models import BlogCategory, Blog, BlogComment


# Register your models here.
class BlogCategoryAdmin(admin.ModelAdmin):
    # 这个模型中哪些字段是可以被编辑的
    list_display = ['name']


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'publish_time', 'category', 'author')


class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'publish_time', 'blog', 'author')


# 管理BlogCategory这个模型的时候 用的是BlogCategoryAdmin这个Admin
admin.site.register(BlogCategory, BlogCategoryAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(BlogComment, BlogCommentAdmin)


