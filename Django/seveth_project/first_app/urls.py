from django.urls import path
# from . import views

from first_app.views import Home
urlpatterns = [ 
    
    path('', Home, name ="homepage")
]