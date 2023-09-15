from django.shortcuts import render

# Create your views here.

def home(request):
#    count = int(request.COOKIES.get('count', 0))
#    count = count + 1 
#    response = render(request, 'testapp/count.html', {'count':count})
#    response.set_cookie('count', count)
#    return response

    if 'count' in request.COOKIES:
        new_count = int(request.COOKIES['count']) + 1
    else:
        new_count = 1
    response = render(request, 'testapp/count.html',{'count':new_count})
    response.set_cookie('count', new_count)
    return response