from django import forms
from django.contrib.auth.models import User
from .models import Book , profile
from django.contrib.auth.forms import UserCreationForm




class UserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class PostForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('name', 'master','field','university','status','status2','price','description',)


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = profile
        fields = ['image']