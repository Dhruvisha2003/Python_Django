from django.db import models

# Create your models here.

class Menu(models.Model):
    name = models.CharField(max_length=25)
    url = models.FileField()

class products(models.Model):
    picture = models.ImageField()
    name = models.CharField(max_length=20)
    price = models.CharField(max_length=10)

class pdetails(models.Model):
    photo = models.ImageField()
    name = models.CharField(max_length=20)
    detail = models.CharField(max_length=220)
    link = models.CharField(max_length=20)

class shop(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=20)
    price = models.CharField(max_length=10)