from django import forms
from blogapp.models import Profile

class SignUpForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['name','email','password','date_of_birth','proffession']

class LoginForm(forms.Form):
    username=forms.CharField(max_length=255)
    password=forms.CharField(max_length=20)


class PostForm(forms.Form):
        title=forms.CharField(max_length=255)
        body=forms.CharField(widget=forms.Textarea)
        comment=forms.TextInput()