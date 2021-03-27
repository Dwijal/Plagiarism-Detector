from django.db import models

# Create your models here.
class user(models.Model):
    rollno = models.CharField(max_length=8, unique=True)
    password = models.CharField(max_length=20)

class assign(models.Model):
    roll = models.CharField(max_length=8, unique=True)
    file = models.FileField(upload_to='upload/am/')

class rep(models.Model):
    rollno = models.CharField(max_length=8, unique=True)
    score = models.CharField(max_length=3)
    mess = models.CharField(max_length=100)
