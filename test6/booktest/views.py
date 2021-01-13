from django.shortcuts import render
from django.conf import settings
# Create your views here.

def static_test(request):
    '''静态文件'''
    return render(request, 'booktest/static_test.html')

EXCLUDE_IPS = ['172.16.179.152']
def index(request):
    '''首页'''
    #获取浏览器端的Ip地址
    # user_ip = request.META['REMOTE_ADDR']
    # print(user_ip)
    return render(request, 'booktest/index.html')