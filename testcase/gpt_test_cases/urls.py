from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.home),
    path('generate/', views.generate),
    path('generate-image/', views.generate_image),

    
]