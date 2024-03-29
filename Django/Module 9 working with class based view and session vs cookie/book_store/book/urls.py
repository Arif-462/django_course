from django.urls import path
# from book.views import home, store_book, edit_book,show_book, delete_book
from . import views
urlpatterns = [  
    # path('', views.home, name = 'home'),
    # path('', views.TemplateView.as_view(template_name = 'home.html'), name='home'),
    path('', views.MyTemplateView.as_view(),{'roll':1,'author':'Arif'}, name = 'home'),
    # path('store_new_book/', views.store_book, name = 'store_book'),   
    path('store_new_book/', views.BookFormView.as_view(), name = 'store_book'),   
    # path('show_books/',views.show_book, name = 'show_book'),
    path('show_book/',views.bookListView.as_view(), name = 'show_book'),
    path('book_details/<int:id>',views.BookDetailsView.as_view(), name = 'Book_details'),
    # path('edit_book/<int:id>',views.edit_book, name = 'edit_book'),
    path('edit_book/<int:pk>',views.BookUpDateview.as_view(), name = 'edit_book'),
    # path('delete_book/<int:id>', views.delete_book, name = 'delete_book'),
    path('delete_book/<int:pk>', views.DeleteBookView.as_view(), name = 'delete_book'),
    
]
