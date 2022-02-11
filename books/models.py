from unicodedata import category
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    image_url = models.CharField(max_length=100)
    name = models.CharField(max_length=150)
    author = models.CharField(max_length=50)
    isbn = models.IntegerField()
    category = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"

class Favourite(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)