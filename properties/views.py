from django.shortcuts import render
from .models import Property


def property_list_view(request):
    properties = Property.objects.all()
    return render(request, 'property/property_list.html', {"properties":properties} )

def createproperty(request):
    return render(request, "property/create_property.html")

def updateproperty(request):
    return render(request, "property/update_property.html")

def deleteproperty(request):
    return render(request, "property/detete_property.html")
    

    
    

