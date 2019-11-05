from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
class Insertdata(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),label='Confirm Password')
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}),label='Email')

    class Meta:
        model=User
        fields=['username','password1','password2','email']