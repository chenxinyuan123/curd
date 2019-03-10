from django.db import models

# Create your models here.

class User(models.Model):
    user = models.CharField(max_length=16)
    pwd=models.CharField(max_length=16)
    age=models.IntegerField()
    hobby=models.CharField(max_length=32)
    salary=models.IntegerField()