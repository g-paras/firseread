from django.urls import path

from . import views

urlpatterns = [
    path("", views.home_view, name="home"),
    path("books/fav/", views.fav_view, name="favourite"),
    path("books/fav/add/<int:isbn>", views.add_to_fav, name="addtofav"),
    path("books/fav/remove/<int:isbn>", views.remove_fav, name="removefav"),
]
