from .models import ProprietorProfile
from django.forms.models import ModelForm 
from django import forms

class ProprietorProfileForm(ModelForm):
    cni_recto = forms.FileField(label='NID front', required=True)
    cni_recto = forms.FileField(label='NID back', required=True)
    facture_recto = forms.FileField(label='Water or electric bill front', required=True)
    facture_verso = forms.FileField(label="Bill back")
    
    class Meta:
        model=ProprietorProfile
        fields=["cni_recto", "cni_verso", "facture_recto", "facture_verso"]
