from django.db import models

# Create your models here.

class user_data(models.Model):
    fname=models.CharField(max_length=50)
    fname=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    mob=models.CharField(max_length=50)
