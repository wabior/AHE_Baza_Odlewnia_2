"""Django_Project_Baza URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import include, path
from App_Baza.views import  machine_create_view, raport_view, NewUser_view, raporty_view, formy_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('App_Baza.urls')),
    path('create/', machine_create_view, name='create'),
    path('raport/', raport_view, name='raport'),
    path('user/', NewUser_view, name='user'),
    path('raporty/', raporty_view, name='raporty'),
    path('formy/', formy_view, name='formy'),



]
