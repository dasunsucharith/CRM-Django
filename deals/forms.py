from django import forms
from .models import Deal

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
