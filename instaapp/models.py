from django.db import models

# Create your models here.

class Profile(models.Model):
    username = models.CharField(max_length=30)
    email = models.CharField(max_length=150)
    password = models.CharField(max_length=100)

class Photo(models.Model):
    photo