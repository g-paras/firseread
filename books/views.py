from django.shortcuts import render, redirect

from .models import Book, Favourite

# Create your views here.
def home_view(request):
    books = Book.objects.all()[:50]
    favs = []
    if request.user.is_authenticated:
        favs = Favourite.objects.filter(user=request.user)
    return render(request, "home.html", {"books": books, "favs": favs})


def fav_view(request):
    if request.user.is_authenticated:
        user = request.user
        favs = Favourite.objects.filter(user=user)
        return render(request, "favourite.html", {"favs": favs})
    return redirect("login")


def add_to_fav(request, isbn):
    if request.user.is_authenticated:
        book = Book.objects.filter(isbn=isbn).first()
        fav = Favourite()
        fav.user = request.user
        fav.book = book
        fav.save()
        return redirect("home")
    return redirect("login")


def remove_fav(request, isbn):
    if request.user.is_authenticated:
        book = Book.objects.filter(isbn=isbn).first()
        fav = Favourite.objects.filter(user=request.user, book=book)
        fav.delete()
        return redirect("favourite")
    return redirect("login")
