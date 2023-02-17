from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post

class SignupForm(UserCreationForm):
    email=forms.EmailField()

    class Meta:
        model=User
        fields=['username','email','password1','password2']

# class PostForm(forms.Form):
#     author=forms.CharField(max_length=255)
#     title=forms.CharField(max_length=255)
#     post=forms.TextInput()

class PostForm(forms.ModelForm):
    # author=forms.CharField(max_length=255)
    # title=forms.CharField(max_length=255)
    # post=forms.TextInput()
    class Meta:
       model=Post
       fields=['author','title','description']
