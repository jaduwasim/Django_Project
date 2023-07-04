from django.shortcuts import render

# Create your views here.

def Static_Views(request):
    my_dict = {'static':'Static Page'}
    return render(request, 'testapp/static_view.html', my_dict)