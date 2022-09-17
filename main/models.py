from django.db import models

# Create your models here.
class ServiceIcon(models.Model):
    Icon1 = models.CharField(max_length=40)
    Icon2 = models.CharField(max_length=40)
    Icon3 = models.CharField(max_length=40)
    Icon4 = models.CharField(max_length=40)
    Icon5 = models.CharField(max_length=40)
    Icon6 = models.CharField(max_length=40)
    Icon1Desc = models.CharField(max_length=600)
    Icon2Desc = models.CharField(max_length=600)
    Icon3Desc = models.CharField(max_length=600)
    Icon4Desc = models.CharField(max_length=600)
    Icon5Desc = models.CharField(max_length=600)
    Icon6Desc = models.CharField(max_length=600)
class Portfolio(models.Model):
    name = models.CharField(max_length=40)
    image = models.ImageField(upload_to='Portfolio/')
    field = models.CharField(max_length=50)
    url = models.CharField(max_length=5000)
class AboutUs(models.Model):
    head = models.CharField(max_length=40)
    about = models.CharField(max_length=700)
    Link4btn = models.CharField(max_length=5000)
    other = models.CharField(max_length=900)
class Enquiry(models.Model):
    name = models.CharField(max_length=40)
    number = models.CharField(max_length=22)
    email = models.CharField(max_length=50)
    msg = models.CharField(max_length=7000)