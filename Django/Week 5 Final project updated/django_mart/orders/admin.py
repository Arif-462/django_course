from django.contrib import admin
from .models import Payment, Order, Orderproduct, PaymentGatewaySettings

# Register your models here.
admin.site.register(Payment)
admin.site.register(Order)
admin.site.register(Orderproduct)
admin.site.register(PaymentGatewaySettings)
