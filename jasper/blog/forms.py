from django import forms
from django.contrib.auth.models import User
from .models import Book
from django.contrib.auth.forms import UserCreationForm




class userform2(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username','email')

#class UserForm(forms.ModelForm):
    #class Meta:
        #model = User
        #exclude = ['description']

class PostForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('name','description', 'price','master','field','status','university')