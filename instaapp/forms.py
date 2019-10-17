from django import forms
from .models import Photo


class InstagramLetterForm(forms.Form):
    your_username = forms.CharField(label='Your Username',max_length=30)
    email = forms.EmailField(label='Email')

class NewPhotoForm(forms.modelForm):
    class Meta:
        model = Photo
        # exclude = ['']
    widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }    