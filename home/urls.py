from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('delivery/', views.delivery, name='delivery'),
    path('about_us/', views.about_us, name='about_us'),    
]
