from django.urls import path
# from . import views

from first_app.views import Home, showData
urlpatterns = [ 
    
    path('', Home, name ="homepage"),
    path('show/', showData, name='showData')
]