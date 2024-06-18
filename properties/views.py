from django.shortcuts import render, redirect
from .models import Property
from .forms import PropertyForm


def property_list_view(request):
    properties = []
    for property in Property.objects.all():
        if len(property.rooms.all()) == 0:
            return
        properties.append(property)
    return render(request, 'property/property_list.html', {"properties":properties} )

def property_create_view(request):
    form = PropertyForm()
    context = {
        "form": form
    }
    
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            property = form.save(commit=False)
            property.proprietor = request.user.proprietorprofile
            property.save()
            return redirect('property-list')
    
    return render(request, "property/create_property.html", context)

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

    
    

