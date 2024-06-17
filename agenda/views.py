from django.shortcuts import render

def createvisit(request):
    return render(request, "visit/create_visit.html")


def cancelvisit(request):
    return render(request,"visit/cancel_visit.html")

# Create your views here.
