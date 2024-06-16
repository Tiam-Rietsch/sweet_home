from .models import ProprietorProfile
from django.forms.models import ModelForm 

class ProprietorProfileForm(ModelForm):
    
    class Meta:
        model=ProprietorProfile
        fields=["cni_recto", "cni_verso", "facture_recto", "facture_verso","status"]
