from django.forms import TextInput, EmailInput, Textarea

from .models import Contacts
from django import forms

class ContactsForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = ['name', 'email', 'phone_number', 'message']

        widgets = {
            'name': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Full name'
                }),
            'email': EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Email'
                }),
            'phone_number': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Phone number'
                }),
            'message': Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Message'
                }),
        }