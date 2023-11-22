from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('delivery/', views.delivery, name='delivery'),
    path('returns/', views.returns, name='returns'), 
    path('about_us/', views.about_us, name='about_us'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
]
