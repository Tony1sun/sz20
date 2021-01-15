from django.shortcuts import render
from django.conf import settings
# Create your views here.

def static_test(request):
    '''静态文件'''
    return render(request, 'booktest/static_test.html')

def index(request):
    '''首页'''
    print('---index---')
    num = 'a' + 1
    return render(request, 'booktest/index.html')