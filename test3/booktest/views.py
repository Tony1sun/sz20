from django.shortcuts import render
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
