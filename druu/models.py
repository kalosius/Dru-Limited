from django.db import models
import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# creating customer profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_modified = models.DateTimeField(User, auto_now=True)
    phone = models.CharField(max_length=20, blank=True)
    address1= models.CharField(max_length=200, blank=True)
    address2= models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)
    state = models.CharField(max_length=200, blank=True)
    zipcode = models.CharField(max_length=200, blank=True)
    country = models.CharField(max_length=200, blank=True)
    old_cart = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.user.username
    
# create profile on default when user signs up
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
    
# automating the profile
post_save.connect(create_profile, sender=User)




# categories of products
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
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    
    def __str__(self):
        return self.name



# GENDER = [(('male'),('female'))]

class Partner(models.Model):
    GENDER_CHOICES = [('M', 'Male'),('F', 'Female'),]

    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    birth_date = models.DateField(null=True, blank=True)
    position = models.CharField(max_length=50)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    partner_image = models.ImageField(upload_to="uploads/partners/", default="")
    partner_blog = models.TextField(max_length=5000, null=True, blank=True)
    social_url = models.URLField(max_length=2856,   null=True, blank=True)
    age = models.IntegerField(default='', null=True, blank=True)
    contact = models.CharField(max_length=30, default='', blank=True, null=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}" 

    
