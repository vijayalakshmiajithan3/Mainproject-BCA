from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserType(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    type = models.CharField(max_length=50,null=True)

class user_reg(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    address = models.CharField(max_length=50,null=True)
    phone = models.CharField(max_length=50,null=True)

class merchant_reg(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    address = models.CharField(max_length=50,null=True)
    phone = models.CharField(max_length=50,null=True)

class farmer_reg(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    address = models.CharField(max_length=50,null=True)
    phone = models.CharField(max_length=50,null=True)

class merch_thread(models.Model):
    merchant = models.ForeignKey(merchant_reg, on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=50,null=True)
    price = models.CharField(max_length=50,null=True)
    description = models.CharField(max_length=150,null=True)
    status = models.CharField(max_length=50,null=True)
    image = models.ImageField(null=True)

class farmer_thread(models.Model):
    farmer = models.ForeignKey(farmer_reg, on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=50,null=True)
    price = models.CharField(max_length=50,null=True)
    description = models.CharField(max_length=150,null=True)
    status = models.CharField(max_length=50,null=True)
    image = models.ImageField(null=True)


class merch_cart(models.Model):
    thread = models.ForeignKey(merch_thread, on_delete=models.CASCADE,null=True)
    user = models.ForeignKey(user_reg, on_delete=models.CASCADE,null=True)
    status = models.CharField(max_length=50,null=True)
    track = models.CharField(max_length=50,null=True)


class farmer_cart(models.Model):
    thread = models.ForeignKey(farmer_thread, on_delete=models.CASCADE,null=True)
    user = models.ForeignKey(user_reg, on_delete=models.CASCADE,null=True)
    status = models.CharField(max_length=50,null=True)


class mfeedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    mcart = models.ForeignKey(merch_cart, on_delete=models.CASCADE, null=True)
    feedback = models.CharField(max_length=50,null=True)
