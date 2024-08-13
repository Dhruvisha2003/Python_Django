from django.db import models

# Create your models here.

class stud(models.Model):
    name = models.TextField(max_length=255)
    marks1 = models.IntegerField()
    marks2 = models.IntegerField()
    marks3 = models.IntegerField()
    marks4 = models.IntegerField()
    marks5 = models.IntegerField()
    total = models.IntegerField()
    percentage = models.IntegerField()
    grade = models.TextField(max_length=6)
    min_marks = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
