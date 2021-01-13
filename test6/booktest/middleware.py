from django.http import HttpResponse

class BlockedIPSMiddleware:
    EXCLUDE_IPS = ['172.16.179.152']
    def process_view(self, request, view_func, *view_args, **view_kwargs):
        '''视图函数调用之前调用'''
        user_ip = request.META['REMOTE_ADDR']
        if user_ip in BlockedIPSMiddleware.EXCLUDE_IPS:
            return HttpResponse('<h1>Forbidden</h1>')