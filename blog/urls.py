from django.urls import path
from . import views

urlpatterns = [
    path('', views.volume_list, name='volume_list'),
    path('volume/<int:pk>/', views.volume_detail, name='volume_detail'),
    path('spanish/', views.spanish_volume_list, name='spanish_volume_list'),
    path('about/', views.about, name='about'),
    path('spanish-about/', views.spanish_about, name='spanish_about'),
    path('spanish-volume/<int:pk>/', views.spanish_volume_detail, name='spanish_volume_detail'),
]