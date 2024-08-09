from django.db import models

# Create your models here.

gender_choices=(('male',"Male"),
                ('female',"Female"))

class User(models.Model):
    name = models.TextField(max_length=255)
    contact = models.BigIntegerField()
    gender = models.TextField(max_length=10,choices=gender_choices)
    email = models.EmailField(max_length=255, unique=True)
    password = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)