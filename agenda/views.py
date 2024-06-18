from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import VisitForm
from properties.models import Property

@login_required(login_url='login')
def program_visit_view(request):
    form = VisitForm()
    property = Property.objects.get(id=int(request.GET.get('property_id')))
    context = {
        "form": form,
        "property": property,
        "main_image": property.rooms.all()[0].image
    }
    
    if request.method == "POST":
        form = VisitForm(data=request.POST)
        if form.is_valid():
            visit = form.save(commit=False)
            visit.buyer_profile = request.user.buyerprofile
            visit.property = property
            visit.save()
        return redirect('property-detail', property.id)
    
    return render(request, "visit/program_visit.html", context)


def cancelvisit(request):
    pass

# Create your views here.
