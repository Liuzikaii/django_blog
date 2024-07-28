# 项目介绍
使用Django搭建个人博客，前端使用Django中的模板实现。
样式使用Bootstrap(提供CSS和JS工具)
Django官网：https://docs.djangoproject.com/en/5.0/
Bootstrap示例：https://v5.bootcss.com/docs/examples/
# 项目所用技术栈
- 前端：Bootstrap、Jquery
- 后端：Django
- 基础：Javascript、Css、Html
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

