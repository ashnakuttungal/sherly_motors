from django.db import models

# Create your models here.
class cardetails(models.Model):
    carname=models.CharField(max_length=200)
    carmodel=models.CharField(max_length=200)
    caryear=models.CharField(max_length=200)
    carprice=models.CharField(max_length=200) 
    carmlg=models.CharField(max_length=200)  
    carphoto=models.ImageField()
