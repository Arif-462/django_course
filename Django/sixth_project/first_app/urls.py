from django.urls import path
from . import views

urlpatterns = [   
    path('', views.Home, name = 'homepage'),
    path('delete/<int:roll>', views.delete_student, name = 'delete_student')
]