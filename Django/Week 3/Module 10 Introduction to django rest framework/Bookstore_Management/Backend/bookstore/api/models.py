from django.db import models

# Create your models here.

class BookStoreModel(models.Model):
    id = models.IntegerField(primary_key=True)
    Book_name = models.CharField(max_length=30)
    author = models.CharField(max_length=20)
    
    CATEGORY = (
        ('Mystery', 'Mystery'),
        ('Thriller', 'Thriller'),
        ('Sci-fi', 'Sci-fi'),
        ('Humor', 'Humor'),
        ('Horror', 'Horror'),
    )
    
    category = models.CharField(max_length=30, choices= CATEGORY)
    first_pub = models.DateTimeField(auto_now_add=True) # django ekdom first date
    last_pub = models.DateTimeField(auto_now=True)# erpore joto update korbo update hobe