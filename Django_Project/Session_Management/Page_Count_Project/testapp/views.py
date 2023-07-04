from django.shortcuts import render

# Create your views here.
def Page_Count_View(request):
    count = int(request.COOKIES.get('count',0))
    count = count+1
    response = render(request, 'testapp/page_count.html', {'count':count})
    response.set_cookie('count',count)
    return response