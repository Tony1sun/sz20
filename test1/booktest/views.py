from django.shortcuts import render
from django.http import HttpResponse
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