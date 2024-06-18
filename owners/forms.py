from django import forms
from django.contrib.auth.models import User
from api.models import Products 

class Loginform(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

class Signupform(forms.ModelForm):
    class Meta:
        model=User
        fields=["first_name","last_name","username","email","password"]

class AddProductForm(forms.ModelForm):
    class Meta:
        model=Products
        fields= "__all__"
