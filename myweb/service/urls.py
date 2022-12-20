from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.homePage, name='home'),
    path('data/', views.dataPage, name='data'),
    path('search/', views.searchPage, name='search'),
    path('search/pie/', views.piePage, name='pie'),
    path('search/pie/chart', views.chartPage, name='chart'),
    path('search/pie/chart/precedent', views.precedent, name='precedent'),
    path('search/pie/chart/precedent/nextPage', views.nextPage, name='nextPage')
]

