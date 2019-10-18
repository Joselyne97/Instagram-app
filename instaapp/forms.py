from django import forms
from .models import Profile


class InstagramLetterForm(forms.Form):
    your_username = forms.CharField(label='Your Username',max_length=30)
    email = forms.EmailField(label='Email')

