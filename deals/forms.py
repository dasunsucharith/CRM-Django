from django import forms


class DealForm(forms.Form):
    contact_person = forms.CharField()
    organization = forms.CharField()
    title = forms.CharField()
    value = forms.IntegerField(min_value=0)
    phone = forms.CharField()
    email = forms.CharField()
