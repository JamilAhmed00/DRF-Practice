

from django.contrib import admin
from django.urls import path
from app1 import views


urlpatterns = [
     
        path('studentapi/', views.StudentAPI.as_view()),
        path('studentapi/<int:pk>/', views.StudentAPI.as_view()),
    
    
]
