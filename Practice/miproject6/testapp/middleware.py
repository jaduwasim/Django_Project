
class CustomMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        print()
        print('This Code Execute at the time of Server Running')
    
    def __call__(self, request):
        print()
        print('This Code Executing before the request processing')
        response = self.get_response(request)
        print('This code Executing after request Processing!!!')
        return response