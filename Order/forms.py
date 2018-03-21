from django import forms
from .models import Buyer

class OrderForm(forms.ModelForm):
    class Meta:
        model = Buyer
        fields = ['name', 'tel', 'address']
