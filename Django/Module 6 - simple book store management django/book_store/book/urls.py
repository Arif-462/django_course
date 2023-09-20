from django.urls import path
from book.views import home, store_book, edit_book,show_books, delete_book

urlpatterns = [  
    path('', home, name = 'home'),
    path('store_new_book/', store_book, name = 'store_book'),   
    path('show_books/',show_books, name = 'show_books'),
    path('edit_book/<int:id>',edit_book, name = 'edit_book'),
    path('delete_book/<int:id>', delete_book, name = 'delete_book'),
    
]
