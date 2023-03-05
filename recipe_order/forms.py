from django import forms
from .models import RecipeOrder


class RecipeOrderForm(forms.ModelForm):
    class Meta:
        model = RecipeOrder
        fields = ('name', 'email', 'recipe_type',
                  'frosting_type', 'delivery_date', 'quantity')
        widgets = {
            'delivery_date': forms.DateInput(attrs={'type': 'date'})
        }
