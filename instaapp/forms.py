from django import forms
from .models import Profile,Image,Comment
from django.contrib.auth.models import User


class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['image_name', 'user', 'profile','comments','likes']   

class NewProfileForm(forms.ModelForm):
    class Meta:
        model= Profile
        exclude =['user']

class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['user','image']