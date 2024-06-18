from django.shortcuts import render
from .models import Property


def property_list_view(request):
    properties = []
    for property in Property.objects.all():
        if len(property.rooms.all()) == 0:
            return
        properties.append(property)
    return render(request, 'property/property_list.html', {"properties":properties} )

def createproperty(request):
    return render(request, "property/create_property.html")

def updateproperty(request):
    return render(request, "property/update_property.html")

def deleteproperty(request):
    return render(request, "property/detete_property.html")
    
def property_detail_view(request, pk):
    property = Property.objects.get(id=pk)
    context = {
        "property": property,
        "main_image": property.rooms.all()[0].image
    }
    return render(request, 'property/property_detail.html', context)

    
    

