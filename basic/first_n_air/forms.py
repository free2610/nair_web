from django import forms
from .models import *

class ChoicesForm(forms.ModelForm):
    class Meta:
        model=Buy
        exclude = ['product']
        fields = '__all__'
    
class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Register
        fields = '__all__'
        exclode = ['message']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = '__all__'
        exclude = ['password','last_name','phone']