from django.shortcuts import render
from django.http import HttpResponse
from booktest.models import BookInfo
from django.template import loader, RequestContext

# Create your views here.
#定义视图函数 建立url地址和试图函数的对应关系
def index(request):

    # return HttpResponse('Hi')
    #加载模板文件
    # temp = loader.get_template('booktest/index.html')
    #定义模板上下文
    # context = RequestContext(request, {})
    #模板渲染
    # res_html = temp.render(context)
    #返回给浏览器
    return render(request, 'booktest/index.html',
                        {'content':'hello world', 'list':list(range(0, 9))})

def index2(request):
    return HttpResponse('Hello python')

def show_books(request):
    '''显示图书的信息'''
    #通过M查找图书表中的数据
    books = BookInfo.objects.all()
    #使用模板
    return render(request, 'booktest/show_books.html', {'books':books})

def detail(request, bid):
    '''查询图书关联的英雄信息'''
    #根据bid查询图书信息
    book = BookInfo.objects.get(id=bid)
    #查询和book关联的英雄信息
    heros = book.heroinfo_set.all()

    return render(request, 'booktest/detail.html',
                  {'book':book,'heros':heros})



