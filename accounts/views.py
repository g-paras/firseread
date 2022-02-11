from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    error=False
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user=user)
            return redirect("home")
        else:
            error = True
    return render(request, "login.html", {"error": error})


def signup_view(request):
    params = {
        'username_error': False,
        'password_error': False,
        'email_error': False,
        'password_error': False,
    }
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        pwd1 = request.POST["password"]
        pwd2 = request.POST["password"]

        if User.objects.filter(username=username).exists():
            params["username_error"] = True
        elif User.objects.filter(email=email).exists():
            params["email_error"] = True
        elif pwd1 != pwd2:
            params['password_error'] = True
        else:
            user = User.objects.create_user(username=username, email=email, password=pwd1)
            user.save()
            return redirect("login")
    return render(request, "signup.html", params)


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("login")
