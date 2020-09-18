from django import forms
from .models import Food, Store

REQUIRED_ERROR_MESSAGE = "You must input this field"


class FoodForm(forms.models.ModelForm):

    class Meta:
        model=Food
        fields=('name', 'description', 'store')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'store': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }
        error_messages={
            'name': {'required': REQUIRED_ERROR_MESSAGE}
        }


class StoreForm(forms.models.ModelForm):

    class Meta:
        model=Store
        fields=('name', 'address')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
        }
        error_messages={
            'name': {'required': REQUIRED_ERROR_MESSAGE},
            'address': {'required': REQUIRED_ERROR_MESSAGE},
        }
