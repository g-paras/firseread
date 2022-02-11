from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from .models import Book, Favourite

# Create your views here.
def login_view(request):
    if request.method=="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user=user)
            return redirect("home")
        else:
            return HttpResponse("Invalid credentials")
    return render(request, "login.html")

def signup_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        pwd1 = request.POST["password"]
        pwd2 = request.POST["password"]

        user = User.objects.create_user(username=username, email=email, password=pwd1)
        user.save()
        return redirect('login')
    return render(request, "signup.html")

def logout_view(request):
    logout(request)
    return redirect("login")

def home_view(request):
    books = Book.objects.all()[:50]
    favs = []
    if request.user.is_authenticated:
        favs = Favourite.objects.filter(user=request.user)
    return render(request, 'home.html', {'books':books, 'favs':favs})

def fav_view(request):
    if request.user.is_authenticated:
        user = request.user
        favs = Favourite.objects.filter(user=user)
        return render(request, "favourite.html", {'favs': favs})
    return redirect('login')

def add_to_fav(request, isbn):
    if request.user.is_authenticated:
        book = Book.objects.filter(isbn=isbn).first()
        fav = Favourite()
        fav.user = request.user
        fav.book = book
        fav.save()
        return redirect('home')
    return redirect('login')

def remove_fav(request, isbn):
    if request.user.is_authenticated:
        book = Book.objects.filter(isbn=isbn).first()
        fav = Favourite.objects.filter(user=request.user, book=book)
        fav.delete()
        return redirect('favourite')
    return redirect('login')