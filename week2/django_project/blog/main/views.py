import imp
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def main(request):
    context = {'like': 'Django 很棒'}  # 範本的動態資料從這送出
    return render(request, 'main.html', context)

def about(request):
    return render(request, 'about.html')