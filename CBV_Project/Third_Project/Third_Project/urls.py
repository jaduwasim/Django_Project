"""Third_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from testapp.views import HomeClass, ClassListView, ClassCreateView, ClassDetailView, ClassUpdateView, ClassDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeClass.as_view()),
    path('list/', ClassListView.as_view(), name='list'),
    path('create/', ClassCreateView.as_view()),
    path('detail/<int:pk>/', ClassDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', ClassUpdateView.as_view()),
    path('delete/<int:pk>/', ClassDeleteView.as_view())
]
