from django import forms
from .models import Teacher
class Addteacher(forms.ModelForm):
    fullname=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    address=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    contact=forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))



    class Meta:
        model =Teacher
        exclude=['user','is_suspend','is_firstlogin']