from django import forms
from .models import Profile,Image
from django.contrib.auth.models import User


class NewImageForm(forms.Form):
    class Meta:
        model = Image
        exclude = [ 'image_name', 'user', 'profile']   

class NewProfileForm(forms.ModelForm):
    class Meta:
        model= Profile
        fields=['bio','profile_pic']
        exclude =['user']

