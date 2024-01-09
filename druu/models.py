from django.db import models
import datetime
from django.db import models
import datetime

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'categories'

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=250, default='', null=True, blank=True)
    image = models.ImageField(upload_to="uploads/products/", default="")
    
    def __str__(self):
        return self.name

# Customer orders
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=100, default='')
    phone_number = models.CharField(max_length=30, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.product


# GENDER = [(('male'),('female'))]

class Partner(models.Model):
    GENDER_CHOICES = [('M', 'Male'),('F', 'Female'),]

    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    birth_date = models.DateField(null=True, blank=True)
    position = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    partner_image = models.ImageField(upload_to="uploads/partners/", default="")
    partner_blog = models.TextField(max_length=5000, null=True, blank=True)
    social_url = models.URLField(max_length=2856,   null=True, blank=True)
    age = models.IntegerField(default='', null=True, blank=True)
    contact = models.CharField(max_length=30, default='', blank=True, null=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}" 

    
