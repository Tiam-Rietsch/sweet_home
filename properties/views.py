from django.shortcuts import render


def property_list_view(request):
    return render(request, 'properties/property_list.html')