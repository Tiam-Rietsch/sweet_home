from django.shortcuts import render, redirect
from .models import User
from .models import BuyerProfile


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
    
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        date_of_birth = request.POST["date_of_birth"]
        phone = request.POST["phone"]
        address = request.POST["address"]
        password = request.POST["password"]
        username = f"{str.lower(first_name).split()[0]}{str.lower(last_name).split()[0]}"
        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            address=address,
            phone=phone,
            email=email
        )
        user.save()

        buyer_profile = BuyerProfile.objects.create(
            user=user
        )
        buyer_profile.save()

        return redirect('login')
