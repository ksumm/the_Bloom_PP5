from django.urls import path
from .views import art_class_list, art_class_detail
from .views import book_art_class, success_view

app_name = 'artclass'

urlpatterns = [
    path('', art_class_list, name='art_class_list'),
    path('<int:art_class_id>/', art_class_detail, name='art_class_detail'),
    path('book/<int:art_class_id>/', book_art_class, name='book_art_class'),
    path('success/', success_view, name='success_view'),
]
