from django import forms
from blog.models import User
from .models import Book
from django.contrib.auth.forms import UserCreationForm




class UserForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ['description']
class PostForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('name','description', 'price','master','field','status','university')