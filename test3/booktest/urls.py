"""test3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from booktest import views

urlpatterns = [
    url(r'^index/', views.index),
    url(r'^showarg(\d+)$', views.show_arg),
    url(r'^login$', views.login),
    url(r'^login_check$', views.login_check),
    url(r'^test_ajax$', views.ajax_test),
    url(r'^ajax_handle$', views.ajax_handle),
    url(r'^login_ajax$', views.login_ajax), #显示ajax登录页面
    url(r'^login_ajax_check$', views.login_ajax_check), # ajax登录校验
    url(r'^set_cookie$', views.set_cookie), #设置cookie
    url(r'^get_cookie$', views.get_cookie), #获取cookie
]
