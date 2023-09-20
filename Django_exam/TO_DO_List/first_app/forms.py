from django import forms
from first_app.models import Task_Model

class Task_Form(forms.ModelForm):
    class Meta:
        model = Task_Model
        fields= ['title', 'description']
        