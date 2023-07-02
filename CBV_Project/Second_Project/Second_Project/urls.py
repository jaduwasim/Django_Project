"""Second_Project URL Configuration

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
from testapp.views import Employee_List, Employee_Create_View, Employee_Detail_View, Employee_Update_View, Employee_Delete_View

urlpatterns = [
    path('admin/', admin.site.urls),
    path('emplist/', Employee_List.as_view(), name='emplist'),
    path('empcreate/', Employee_Create_View.as_view()),
    path('<int:pk>/', Employee_Detail_View.as_view()),
    path('update/<int:pk>', Employee_Update_View.as_view()),
    path('delete/<int:pk>', Employee_Delete_View.as_view()),
]
