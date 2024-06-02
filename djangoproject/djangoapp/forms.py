from django import forms
from .models import ExampleVariety

class ExampleForm(forms.Form):
    exampleVariety = forms.ModelChoiceField(queryset=ExampleVariety.objects.all(),label="Select example variety")