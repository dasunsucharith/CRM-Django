from django import forms
from .models import Deal, User
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model

User = get_user_model()


class DealModelForm(forms.ModelForm):
    class Meta:
        model = Deal
        fields = (
            'contact_person',
            'organization',
            'title',
            'value',
            'phone',
            'email',
            'agent',
        )


class DealForm(forms.Form):
    contact_person = forms.CharField()
    organization = forms.CharField()
    title = forms.CharField()
    value = forms.IntegerField(min_value=0)
    phone = forms.CharField()
    email = forms.CharField()


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}
