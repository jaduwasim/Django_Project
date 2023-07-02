from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.http import HttpResponse

# Create your views here.
class First_Class_Views(View):
    def get(self, request):
        return HttpResponse(
            '<h1>This Resoponse from Class View</h1>'
        )

class Template_View(TemplateView):
    template_name = 'testapp/home.html'