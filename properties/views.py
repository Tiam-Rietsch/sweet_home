from django.shortcuts import render
from .models import Property


def property_list_view(request):
    properties = Property.objects.all()
    return render(request, 'properties/property_list.html', {"properties":properties} )

