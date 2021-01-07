from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
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