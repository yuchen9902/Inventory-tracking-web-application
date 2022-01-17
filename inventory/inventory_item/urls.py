from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:key>/', views.delete, name='delete'),
    path('edit/<int:key>/', views.edit, name='edit'),
    path('export', views.export_csv, name='export'),
]