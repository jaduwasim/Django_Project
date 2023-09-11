from django.shortcuts import render
class Middleware_One(object):
    def __init__(self, get_response):
        self.get_response = get_response
        print('Initialization at the time of running')
    def __call__(self, request):
        return render(request, 'middleware.html')
    # def process_exception(self, request, exeption):
    #     return render(request, 'error.html')

# class Middleware_Second(object):
#     def __init__(self, get_response):
#         self.get_response = get_response
#         print('Executing at the time of server running')

#     def __call__(self, request):
#         print('second Middleware executing before views')
#         response = self.get_response(request)
#         print('Seond Middleware executing after views')
#         return response
    
#     def process_exception(self, request, exception):
#         print('We faced Some Technical Error!')
#         return HttpResponse('<h1>WE FACED SOME TECHNICAL ERROR!</h1>')