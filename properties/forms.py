from .models import Property
from django.forms.models import ModelForm

class PropertyForm(ModelForm):

    class Meta :
        model = Property
        fields = ["land_title", "property_type", "city", "neighborhood", "standing", "price", "description"]