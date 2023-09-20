
# django code in html....

from typing import Any, Dict
from django import forms
from django.core import validators

# widgets == field to html
# form related various attribute:
class contactForm(forms.Form):
    name = forms.CharField(label="Full Name : ", initial="arif",help_text="total length must be 70 characters", required=
    False, disabled=False, widget=forms.Textarea(attrs = {'id' : 'text_area',
    'class': 'class1 class2', 'placeholder': 'Enter your full name'}))
    file = forms.FileField()
    email = forms.EmailField(label="Email")
    # age = forms.IntegerField(label="Age")
    # weight = forms.FloatField(label="Weight")
    # Balance = forms.DecimalField(label="Balance")
    age = forms.CharField(widget=forms.NumberInput)
    check = forms.BooleanField()
    birthday = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    appoinment = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type':'datetime-local'}))
    CHOICES = [('S', 'Small'), ('M', 'Medium'), ('L', 'Large')]
    T_Shirt = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    MEAL = [('P','Pepperoni'), ('M', 'Mashroom'), ('B', 'Beef')]
    Pizza = forms.MultipleChoiceField(choices=MEAL, widget=forms.CheckboxSelectMultiple)

# form validation check:
# class studentData(forms.Form):
#     name = forms.CharField(widget=forms.TextInput)
#     email = forms.CharField(widget=forms.EmailInput)
#     # def clean_name(self):
    #     valname = self.cleaned_data['name']
    #     if len(valname) < 10:
    #         raise forms.ValidationError("Enter atleast 10 chars")
    #     return valname
            
    # def clean_email(self):
    #     valemail = self.cleaned_data['email']
    #     if '.com' not in valemail:
    #         raise forms.ValidationError("Your email must have .com")
    #     return valemail
    
    # def clean(self) -> Dict[str, Any]:
    #     cleaned_data = super().clean()        
    #     valname = self.cleaned_data['name']
    #     valemail = self.cleaned_data['email']
    #     if len(valname) < 10:
    #         raise forms.ValidationError("Enter atleast 10 chars")            
    #     if '.com' not in valemail:
    #         raise forms.ValidationError("Your email must have .com")
        
    
def len_check(value):
    if len(value) < 10:
        raise forms.ValidationError("Enter at least 10 chars!!")
    
class studentData(forms.Form):
    name = forms.CharField(widget=forms.TextInput, validators=[len_check])
    # name = forms.CharField(widget=forms.TextInput, validators=[validators.MaxLengthValidator(50, 'max chars is 50')])
    email = forms.CharField(widget=forms.EmailInput, validators=[validators.EmailValidator('enter a valid email !!')])
    age = forms.IntegerField(widget=forms.NumberInput, validators=[validators.MaxValueValidator(35),validators.MinValueValidator(19)])
    file = forms.FileField(widget=forms.FileInput, validators=[validators.FileExtensionValidator(allowed_extensions=['png'])])


class passwordValidation(forms.Form):
    name = forms.CharField(widget=forms.TextInput)    
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    
    def clean(self):
        cleaned_data = super().clean()
        val_name = self.cleaned_data['name']
        val_password = self.cleaned_data['password']
        re_password = self.cleaned_data['confirm_password']
    
        
        if len(val_name) < 10:
            raise forms.ValidationError("Enter atleast 15 chars!!")
        if val_password is not re_password:
            raise forms.ValidationError("password and confirm password are not matching!!")