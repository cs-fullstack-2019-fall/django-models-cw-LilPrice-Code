from django.db import models

# Create your models here.
class Dog(models.Model):
    Name = models.CharField(max_length=200)
    Breed = models.CharField(max_length=200)
    Color = models.CharField(max_length=200)
    Gender = models.CharField(max_length=200)


class Account(models.Model):
    Username =  models.CharField(max_length=200)
    RealName = models.CharField(max_length=200)
    AccountNumber = models.DecimalField(max_digits = 10, decimal_places = 0)
    Balance = models.DecimalField(max_digits = 10, decimal_places = 2)
