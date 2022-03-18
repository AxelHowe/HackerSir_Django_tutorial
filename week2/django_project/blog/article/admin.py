from django.contrib import admin

# Register your models here.
from article.models import Article, Comment  # 新增

admin.site.register(Article)  # 新增
admin.site.register(Comment)  # 新增
