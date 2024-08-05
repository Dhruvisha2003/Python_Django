from django.db import models

# Create your models here.
class User(models.Model):
    name = models.TextField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    password = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


