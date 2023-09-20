from django.db import models
from store.models import Product
from django.contrib.auth.models import User

# Create your models here.

class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.cart_id
    
class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)# 1 userer multiple cart thakte pare
    # product = models.ForeignKey(Product, on_delete=models.CASCADE) # when various size or color have the product and cart use this foreinker option for one to many relation 
    product = models.ForeignKey(Product, on_delete=models.CASCADE) # only one type item are tobe use for this function
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)
    
    def sub_total(self):
        return self.product.price * self.quantity
    
    def __str__(self):
        return str(self.product)
    
    
