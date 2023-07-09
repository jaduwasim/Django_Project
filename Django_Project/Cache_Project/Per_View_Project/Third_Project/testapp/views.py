from django.shortcuts import render
from django.views.decorators.cache import cache_page
# Create your views here.
@cache_page(60)
def Home(request):
    return render(request, 'testapp/home.html')