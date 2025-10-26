from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Address

# -------------------------------
# Signup Form
# -------------------------------
class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# -------------------------------
# Profile Update Form
# -------------------------------
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone', 'profile_pic', 'date_of_birth']

# -------------------------------
# Address Form
# -------------------------------
class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = [
            'full_name', 'phone', 'address_line_1', 'address_line_2',
            'city', 'state', 'postal_code', 'country', 'address_type', 'is_default'
        ]
