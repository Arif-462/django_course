
from django.urls import path
from . import views

urlpatterns = [    
    path('', views.home, name = 'home'),
    path('show_task/', views.show_task, name='show_task'),
    path('add_task/', views.add_task, name='add_task'),
    path('edit/<int:id>',views.edit_task, name = 'edit_task'),
    path('del_task/<int:id>', views.delete_task, name = 'del_task'),
    # path('complete_task/<int:id>', views.complete_task, name = 'complete_task'),
    path('completed/<int:id>', views.completed_task, name = 'completed'),
    path('completed/', views.completed_task_list, name = 'completed_all'),
]
