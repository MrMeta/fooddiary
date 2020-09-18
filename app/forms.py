from django import forms

from .models import Food

REQUIRED_ERROR_MESSAGE = "You must input this field"


class FoodForm(forms.models.ModelForm):

    class Meta:
        model=Food
        fields=('name', 'description')
        error_messages={
            'name': {'required': REQUIRED_ERROR_MESSAGE}
        }
