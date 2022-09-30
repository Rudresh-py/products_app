from django import forms
from .models import Product, Rating


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product

        fields = '__all__'


class RateForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ('rate_range', 'rating')
