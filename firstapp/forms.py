from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,UsernameField,PasswordChangeForm,SetPasswordForm,PasswordResetForm
from django.contrib.auth.models import User

from .models import Customer

import re
from django import forms
from django.core.exceptions import ValidationError

from django import forms
from .models import Customer

def validate_gmail_email(value):
    pattern = r'^[a-zA-Z][a-zA-Z0-9]*@gmail\.com$'
    if not re.match(pattern, value):
        raise ValidationError("Email must start with a letter and contain only letters and numbers, ending with @gmail.com")

# def validate_gmail_email(value):
# pattern = r'^[a-zA-Z0-9]+@gmail\.com$'
# if not re.match(pattern, value):
# raise ValidationError("Email must be letters and numbers only, ending with @gmail.com")

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus': 'True',
    'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput
    (attrs={'autocomplete':'current-password','class': 'form-control'}))



# class CustomerRegistrationForm(UserCreationForm):
#     username = forms.CharField(widget=forms.TextInput(attrs={'autofocus':'True',
#     'class': 'form-control'}))
#     email = forms.EmailField(widget=forms.EmailInput(attrs=
#     {'class': 'form-control'}))
#     password1 = forms.CharField( label='Password', widget=forms.PasswordInput
#     (attrs={'class':'form-control'}))
#     password2 = forms.CharField(label=' Confirm Password', widget=forms.PasswordInput
#     (attrs={'class': 'form-control'}))

class CustomerRegistrationForm(UserCreationForm):
    username = forms.CharField(
    widget=forms.TextInput(attrs={
        'autofocus': 'True',
        'class': 'form-control',
        'onkeydown': "if(event.key === ' ') event.preventDefault();"
    })
) 
    # username = forms.CharField(widget=forms.TextInput(attrs={'autofocus':'True', 'class': 'form-control'}))
    email = forms.EmailField(
        validators=[validate_gmail_email],
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username','email','password1','password2']


    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Old Password',widget=forms.PasswordInput
    (attrs={'autofocus':'True','autocomplete':'current-password','class':'form-control'}))
    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput
    (attrs={'autocomplete': 'current-password', 'class': 'form-control'}))
    new_password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput
    (attrs={'autocomplete': 'current-password', 'class': 'form-control'}))

class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))


class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(attrs={'autocomplete': 'current-password','class':'form-control'}))
    new_password2 = forms.CharField(label='Confirm New Password', widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class': 'form-control'}))


# class CustomerProfileForm(forms.ModelForm):
#     class Meta:
#         model = Customer
#         fields = ['name','locality','city','mobile','state','zipcode']
#         widgets={
#             'name': forms.TextInput(attrs={'class':'form-control'}),
#             'locality': forms.TextInput(attrs={'class': 'form-control'}),
#             'city': forms.TextInput(attrs={'class': 'form-control'}),
#             'mobile': forms.NumberInput(attrs={'class': 'form-control'}),
#             'state': forms.Select(attrs={'class': 'form-control'}),
#             'zipcode': forms.NumberInput(attrs={'class': 'form-control'}),
#         }


class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'locality', 'city', 'mobile', 'zipcode', 'country']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'locality': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control'}),  # changed from NumberInput
            'zipcode': forms.NumberInput(attrs={'class': 'form-control'}),
            'country': forms.Select(attrs={'class': 'form-control'}),   # changed from 'state' to 'country'
        }
