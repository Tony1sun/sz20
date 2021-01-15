from django.http import HttpResponse

class BlockedIPSMiddleware:
    EXCLUDE_IPS = ['172.16.179.152']
    def process_view(self, request, view_func, *view_args, **view_kwargs):
        '''视图函数调用之前调用'''
        user_ip = request.META['REMOTE_ADDR']
        if user_ip in BlockedIPSMiddleware.EXCLUDE_IPS:
            return HttpResponse('<h1>Forbidden</h1>')


class TestMiddleware:
    '''中间件类'''
    def __init__(self):
        '''服务器重启之后，接受第一个请求时调用'''
        print('---init---')

    def process_request(self, request):
        '''产生request对象之后.url匹配之前调用'''
        print('---process_request---')
        # return HttpResponse('process_request')

    def process_view(self, request, view_func, *view_args,
                     **view_kwargs):
        '''url匹配之后,视图函数调用之前调用'''
        print('---process_view---')
        return HttpResponse('process_view')

    def process_response(self, request, response):
        '''视图函数调用之后，内容返回之前'''
        print('---process_response---')
        return response


class ExceptionTest1Middleware:
    def process_excepion(self, request, excepion):
        print('---process_excepion1---')


class ExceptionTest2Middleware:
    def process_excepion(self, request, excepion):
        print('---process_excepion2---')