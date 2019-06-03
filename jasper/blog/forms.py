from django import forms
from blog.models import User
from django.contrib.auth.forms import UserCreationForm




class UserForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ['description']
