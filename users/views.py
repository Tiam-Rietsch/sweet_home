from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login 


def login_view(request):
    if request.method == "GET":
        return render(request, 'users/login.html')
    
    if request.method == "POST":
        email = request.POST["email"]
        password  = request.POST["password"]
        user =  authenticate(username=email, password=password)
        if user is None:
            message = "email or password incorect"
            return render(request, 'users/login.html', {'message': message})
        else :
            login(request, user)
            return redirect('property-list')
            


def signup_view(request):
    if request.method == "GET":
        return render(request, 'users/signup.html')
    
    # if request.method == "POST"