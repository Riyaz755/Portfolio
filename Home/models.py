from django.db import models

# Create your models here.

class contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=12)
    phone=models.CharField(max_length=10)
    desc=models.CharField(max_length=50)
