from django.db import models
from django.conf import settings


# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=20)
    age = models.CharField(max_length=3)
    description = models.CharField(max_length=100)


  

    def __str__(self):
        return self.name + " " + gender

class CustomerOrder(models.Model):
    name = models.CharField(max_length=100)
    product = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    size = models.CharField(max_length=2)
    choice = models.CharField(max_length=10)


    def __str__(self):
        return self.name + " " + product

class Customerdetails(models.Model):
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    gmail = models.EmailField()
    gender = models.CharField(max_length=100)
    date = models.TextField(max_length=100)


    def __str__(self):
        return self.name + " " + f_name

