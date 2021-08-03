from django import forms
from .models import *

class imgfrom(forms.ModelForm):
    class Meta:
        models = Stock_Me
        fields = ['img']