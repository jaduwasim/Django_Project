from django.urls import path
from .views import Static_Views

urlpatterns = [
    path('static/', Static_Views)
]