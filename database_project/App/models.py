from django.db import models

# Create your models here.
class User(models.Model):
    name = models.TextField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    password = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

gender_choices=(('male',"Male"),
                ('female',"Female"))


class register(models.Model):
    name = models.TextField(max_length=255)
    gender = models.TextField(max_length=10,choices=gender_choices)
    email = models.EmailField(max_length=255, unique=True)
    password = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
