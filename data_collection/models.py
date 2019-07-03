from django.db import models

# Create your models here.
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()

class Data(models.Model):
