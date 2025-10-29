from django import forms
from .models import Checkout

class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Checkout
        fields = ['full_name', 'phone_number', 'address', 'payment_method']
        widgets = {
            'address': forms.Textarea(attrs={'rows': 3}),
        }