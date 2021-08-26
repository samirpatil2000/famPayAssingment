from .models import API

from django import forms

class FilterForm(forms.ModelForm):

    class Meta:
        model=API
        fields=[
            'category',
            'name',
        ]