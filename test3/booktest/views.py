from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from datetime import datetime,timedelta
# Create your views here.
def index(request):
    # num = 'a' + 1
    return render(request, 'booktest/index.html')

def show_arg(request, num):
    return HttpResponse(num)

def login(request):
    '''获取cookie.username'''
    if 'username' in request.COOKIES:
        #获取记住的用户名
        username = request.COOKIES['username']
    else:
        username = ''
    return render(request, "booktest/login.html",
            {'username':username})

def login_check(request):
    '''登录校验视图'''
    #获取提交的用户名和密码
    username = request.POST.get('username')
    password = request.POST.get('password')
    remember = request.POST.get('remember')
    # print(remeber)
    # print(username + ':' + password)
    #进行登陆的校验
    if username == 'admin' and password == '123456':
        #用户名密码正确，跳转到首页
        response =  redirect('/index')
        #判断是否需要记住用户名
        if remember == 'on':
            #设置cookie
            response.set_cookie('username',username,
                    max_age=7*24*3600)
        return response
    else:
    #返回应答
        return redirect('/login')

def ajax_test(request):
    '''显示ajax页面'''
    return render(request, 'booktest/test_ajax.html')

def ajax_handle(request):
    num = 'a' + 1
    return JsonResponse({'res':1})

def login_ajax(request):
    '''显示ajax登录页面'''
    return render(request, 'booktest/login_ajax.html')

def login_ajax_check(request):
    '''ajax登录校验'''
    #获取用户名和密码
    username = request.POST.get('username')
    password = request.POST.get('password')
    #进行校验
    if username == 'admin' and password == '123456':
        return JsonResponse({'res':1})
    else:
        return JsonResponse({'res':0})

def set_cookie(request):
    '''设置cookie信息'''
    response = HttpResponse('设置cookie')
    response.set_cookie('num', 1, max_age=14*24*3600)
    # response.set_cookie('num', 1,expires=datetime.now()+timedelta(dats=14))
    return response

def get_cookie(request):
    '''获取cookie信息'''
    num = request.COOKIES['num']
    return HttpResponse(num)