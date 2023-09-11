from typing import Any
from django.http import HttpResponse

def My_Middleware(get_response):
    print()
    print('This Code Execute at the Time of Server Running')
    def Middlware_One(request):
        print('This code extcute before Views Logic')
        reponse = get_response(request)
        print('This code Excute after views logic execution')
        return reponse
    
    return Middlware_One


class MiddlewareClass:
    def __init__(self,get_response):
        print('-------------')
        print('At the time of Server Running')
        self.get_response = get_response

    # def __call__(self, request):
    #     print('============')
    #     print('execution this code before views execution......')
    #     response = self.get_response(request)
    #     print('===================')
    #     print('Execetion after views code execution.......1')
    #     return response
    def __call__(self,request):
        return HttpResponse('<h1>Response from Middleware</h1>')
    
    def process_exception(self, request, exception):
        return HttpResponse('<h1>Currently we are facing some technical issues!!!!, try after some time</h1>')
