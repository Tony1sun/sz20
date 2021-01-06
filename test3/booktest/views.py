from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
def index(request):
    # num = 'a' + 1
    return render(request, 'booktest/index.html')

def show_arg(request, num):
    return HttpResponse(num)

def login(request):
    return render(request, "booktest/login.html")

def login_check(request):
    '''登录校验视图'''
    #获取提交的用户名和密码
    username = request.POST.get('username')
    password = request.POST.get('password')
    print(username + ':' + password)
    #进行登陆的校验
    if username == 'admin' and password == '123456':
        return redirect('/index')
    else:
    #返回应答
        return redirect('/login')