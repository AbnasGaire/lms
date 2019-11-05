from .models import Manager
from django import forms
class Managerdetail(forms.ModelForm):
    fullname=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    address=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    contact=forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model =Manager
        exclude =['user']
