from django.db import models
from django.shortcuts import render

# Create your models here.

class stud(models.Model):
    name = models.CharField(max_length=150)
    roll_number = models.IntegerField()
    Marks = models.IntegerField()
  

    def __str__(self):
        return self.name
