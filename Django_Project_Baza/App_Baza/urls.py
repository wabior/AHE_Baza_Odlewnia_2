from django.urls import path

from . import views

urlpatterns = [
    path(''         ,   views.index   , name='index'),
    path('nowy_raport', views.nowy_raport  , name='nowy_raport'),
    path('topbar'  ,    views.topbar  , name='topbar'),
]