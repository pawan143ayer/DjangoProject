from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):
    iname=models.CharField(max_length=20)
    quantity=models.IntegerField()
    def __str__(self):
        return self.name

class Unit(models.Model):
    price=models.IntegerField()
    type=models.CharField(max_length=20)

class Customer(models.Model):
    cname=models.CharField(max_length=30)
    address=models.CharField(max_length=50)
    phone=models.CharField(max_length=15)
    email=models.EmailField()
    user  = models.ForeignKey(User)

    def __str__(self):
        return self.cname
class Vendor(models.Model):
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=40)
    phone=models.CharField(max_length=15)
    email=models.EmailField()

    def __str__(self):
        return self.vname

class SalesPurchases(models.Model):
    customer=models.ForeignKey(Vendor,on_delete=models.CASCADE)
    vendor=models.ForeignKey(Customer,on_delete=models.CASCADE)
