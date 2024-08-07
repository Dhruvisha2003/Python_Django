from django.db import models

# Create your models here.
class User(models.Model):
    name = models.TextField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    password = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


GENDER_CHOICES= [
    ('male', 'Male'),
    ('female', 'Female'),
]

class register(models.Model):
    fname = models.TextField(max_length=255)
    lname = models.TextField(max_length=255)
    gender = models.TextField(max_length=6,choices=GENDER_CHOICES)
    email = models.EmailField(max_length=255, unique=True)
    password = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
