from django.db import models

# Create your models here.

class admin(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)


class staff(models.Model):
    staff_id=models.IntegerField(unique=True)
    name=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

class vendor(models.Model):
    vendorname=models.CharField(max_length=100)
    vendor_id=models.IntegerField(unique=True)
    email=models.EmailField()
    vendorpassword=models.CharField(max_length=100)
    productbrought=models.CharField(max_length=255)

class product_add(models.Model):
    product_id=models.AutoField(primary_key=True)
    product_name=models.CharField(max_length=255)
    vendor_name=models.CharField(max_length=100)
    vendor_product_brand=models.CharField(max_length=200)
    describtion=models.TextField()
    category=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    available_quantity=models.IntegerField(default=0)
    manufacture_date=models.DateField(null=True,blank=True)
    #image
    image=models.ImageField(upload_to='photos/')
   

    # created by
    created_by = models.CharField(max_length=100)

class addcart(models.Model):
    customer_id=models.CharField(max_length=200)
    product_id=models.CharField(max_length=200)
    product_name=models.CharField(max_length=255)
    order_quantity=models.IntegerField()
    price=models.DecimalField(max_digits=10,decimal_places=2)

# class ecomuser(models.Model):
#     username=models.CharField(max_length=100,unique=True)
#     password=models.CharField(max_length=100)
#     mail=models.EmailField(null=False,blank=False)

class student(models.Model):
    student_name=models.CharField(max_length=100)
    standard=models.IntegerField(max_length=100)
    doj=models.DateField(null=True,blank=True)
    image=models.ImageField(upload_to='photos/')












