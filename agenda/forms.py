from django import forms
from django.forms.models import ModelForm
from .models import Visit

class VisitForm(ModelForm):
    date_1 = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date"}), label="most preferable date")
    date_2 = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date"}), label="more preferable date")
    date_3 = forms.DateField(required=True, widget=forms.DateInput(attrs={"type": "date"}), label="less preferable date")
        
    class Meta:
        model=Visit
        fields = ["date_1", "date_2", "date_3"]