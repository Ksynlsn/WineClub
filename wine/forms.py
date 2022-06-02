from django import forms
from .models import Country, Region, Wine, Review

class WineForm(forms.ModelForm):
    class Meta:
        model=Wine
        fields='__all__'

class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        fields='__all__'