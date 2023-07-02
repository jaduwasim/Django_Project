"""FB_CRUD_Project URL Configuration

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
from testapp.views import Employee_Views, Employee_List, Employee_Single_Record, Employee_Update_Views, Employee_Delete_Views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Employee_List),
    path('form/', Employee_Views),
    path('<int:id>/', Employee_Single_Record),
    path('update/<int:id>', Employee_Update_Views),
    path('delete/<int:id>', Employee_Delete_Views)
]
