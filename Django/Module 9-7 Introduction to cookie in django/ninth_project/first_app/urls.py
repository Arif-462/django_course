from django.urls import path
from . import views

urlpatterns = [   
    path('', views.set_session),
    path('get/', views.get_cookie),
    path('del/', views.delete_cookie),
    path('get_session/', views.get_session),
    path('del_session/', views.delete_session),
]
