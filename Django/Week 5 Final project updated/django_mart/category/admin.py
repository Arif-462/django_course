from django.contrib import admin
from .models import Catgory

# Register your models here.
# admin.site.register(Catgory)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('category_name',)}
    list_display=('category_name', 'slug')
    
admin.site.register(Catgory, CategoryAdmin)
