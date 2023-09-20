from django.contrib import admin
from first_app.models import Task_Model

# Register your models here.
class TaskModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','description','is_completed')
    
admin.site.register(Task_Model,TaskModelAdmin)

