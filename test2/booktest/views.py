from django.shortcuts import render
from booktest.models import BookInfo
from datetime import date
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
def index(request):
    '''显示图书信息'''
    #查询出所有图书的信息
    books = BookInfo.objects.all()
    #使用模板
    return  render(request, 'booktest/index.html',
                   {'books':books})

def create(request):
    ''''新增一本图书'''
    #创建BookInfo对象
    b = BookInfo()
    b.btitle = '流星蝴蝶剑'
    b.bpub_date = date(1990,1,1)
    #保存
    b.save()
    #返回应答
    return HttpResponseRedirect('/index')