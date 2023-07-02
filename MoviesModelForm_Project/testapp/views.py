from django.shortcuts import render
from testapp.form import Movie_Forms
from testapp.models import Movies_Model

# Create your views here.

def Index_Views(request):
    return render(request, 'testapp/index.html')

def Movies_List_Views(request):
    movies = Movies_Model.objects.all()
    return render(request, 'testapp/list_movies.html', {'movies':movies})

def Movies_Views(request):
    forms = Movie_Forms()
    if request.method == 'POST':
        forms = Movie_Forms(request.POST)
        if forms.is_valid():
            forms.save()
            return render(request, 'testapp/thanks.html')
    return render(request, 'testapp/movies_form.html',{'forms':forms})