from django.shortcuts import render
from booktest.models import BookInfo
# Create your views here.
def index(request):
    '''显示图书信息'''
    #查询出所有图书的信息
    books = BookInfo.objects.all()
    #使用模板
    return  render(request, 'booktest/index.html',
                   {'books':books})