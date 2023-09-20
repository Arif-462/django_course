from django import forms
from first_app.models import StudentModel
# from . import models

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        # all value access
        fields = '__all__'
        # specifiq value access
        # fields = ['name', 'roll']
        # alll value show except roll
        # exclude = ['roll']
        # labels = {
        #     'name': 'Student Name',
        #     'roll': 'Studen Roll'
        # }
        # widgets = {
        #     'name' :forms.TextInput(attrs={'class':'btn-primary'}),
        #     # 'roll':forms.PasswordInput()
            
        # }
        
        # help_texts ={
        #     'name':'write your full name:'
        # }        
        # error_massages={
        #     'name': {'required' :"your name start with md"}
        # }
      
       
    