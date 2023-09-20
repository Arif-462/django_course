from django.urls import path
from . import views

urlpatterns = [   
    path('', views.order_complete, name = 'order_complete'),       
    # path('place_order/', views.order_complete, name = 'order_complete'),       
    path('place_order/', views.place_order, name="place_order"),       
    path('success/', views.success_view, name="sucess"),       
      
 ]
