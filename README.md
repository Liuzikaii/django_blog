# 项目介绍
使用Django搭建个人博客，前端使用Django中的模板实现。
样式使用Bootstrap(提供CSS和JS工具)
Django官网：https://docs.djangoproject.com/en/5.0/
Bootstrap示例：https://v5.bootcss.com/docs/examples/
# 项目所用技术栈
- 前端：Bootstrap、Jquery
- 后端：Django
- 基础：Javascript、Css、Html
- 第三方库（如富文本，编程语言高亮显示）：wangeditor、highlight
# 项目环境
存放于requirements.txt中
使用指令：pip install -r requirements.txt 进行环境的安装
# 邮箱验证码发送配置
## 获取qq邮箱授权码
qq邮箱官网->设置->账号->启用POP3/IMAP/SMTP/Exchange/CardDAV/CalDAV服务->完成短信验证->获得授权码
# 数据库表生成
终端运行:
(1)python ./kk_blog/manage.py makemigrations
(2)python ./kk_blog/manage.py migrate

# Django用户对象
在没有登录的情况下Django使用的是匿名用户登录
# 后台管理系统使用Django自带管理系统
本项目使用Django自带的管理系统，于/admin下
要想在/admin路径下能登录，则需要在auth_user表中将用户设置为是员工
要想在/admin路径下有权限，则需要在auth_user表中将用户设置为是超级管理员

# 后续添加功能
## 用户可自定义头像 头像传至OSS对象存储或图床中
## 增加帖子类型，暂时分为求助帖和分享贴和悬赏贴