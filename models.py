from django.db import models

# Create your models here.
class createaccount(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    password=models.CharField(max_length=12)