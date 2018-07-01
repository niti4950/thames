from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Clients(models.Model):
    first_name=models.CharField(max_length=100,null='True')
    last_name=models.CharField(max_length=100,null='True')
    email=models.EmailField(max_length=100,null='True')
    ph_number=models.IntegerField(null='True')
    address=models.CharField(max_length=100,null='True')
    company_name=models.CharField(max_length=100,null='True')
    gst_no=models.IntegerField(null='True')
    def __str__(self):
        return self.first_name
class Categories(models.Model):
    name=models.CharField(max_length=100)
    slug=models.SlugField(max_length=100)
    def __str__(self):
        return self.name
class Products(models.Model):
    category=models.ForeignKey(Categories)
    name=models.CharField(max_length=100)
    slug=models.SlugField(max_length=100,null='True')
    description=models.TextField(blank=True)
    pic=models.FileField(upload_to='pic',null='True')
    price=models.DecimalField(max_digits=10,decimal_places=2)
    def __str__(self):
        return self.name
