from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
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


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user
