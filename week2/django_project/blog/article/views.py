import re
from django.shortcuts import render

# Create your views here.
# 匯入 Article model
from article.models import Article  # 新增


def article(request):
    # 取出所有文章資料
    articles = Article.objects.all()  # 新增
    context = {'articles': articles}  # 新增
    return render(request, 'article.html', context)
