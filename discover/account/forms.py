from django import forms
from django.core.exceptions import ValidationError
from django.forms import (
    Form,
    ModelForm
)
from django.contrib.auth.models import User


# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Submit
from account.models import (
    Profile
)


class LoginForm(Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput
    )
    confirm_password = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput
    )
    
    class Meta:
        model = User
        fields = [
            'username',
            'email'
        ]
    
    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).exists():
            raise ValidationError('Email already in use.')
        return data

    def clean_confirm_password(self):
        cd = self.cleaned_data
        if cd['password'] != cd['confirm_password']:
            raise ValidationError(f"Passwords don't match.")
        return cd['confirm_password']


class UserEditForm(ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email'
        ]
        
    def clean_email(self):
        data = self.cleaned_data['email']
        qs = User.objects.exclude(
            id=self.instance.id
        ).filter(email=data)
        if qs.exists():
            raise ValidationError('Email already in use.')
        return data


class ProfileEditForm(ModelForm):
    class Meta:
        model = Profile
        fields = [
            'date_of_birth',
            'photo'
        ]