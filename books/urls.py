from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_view, name="home"),
    path('fav/', views.fav_view, name="favourite"),
    path('login/', views.login_view, name="login"),
    path('signup/', views.signup_view, name="signup"),
    path('logout/', views.logout_view, name="logout"),
    path('fav/add/<int:isbn>', views.add_to_fav, name="addtofav"),
    path('fav/remove/<int:isbn>', views.remove_fav, name="removefav")
]