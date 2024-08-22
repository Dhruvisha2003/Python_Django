from django.db import models

class menu(models.Model):
    menu = models.CharField(max_length=12)

class products(models.Model):
    picture = models.ImageField()
    name = models.CharField(max_length=20)
    price = models.CharField(max_length=10)
    
class pdetails(models.Model):
    photo = models.ImageField()
    name = models.CharField(max_length=20)
    detail = models.CharField(max_length=220)