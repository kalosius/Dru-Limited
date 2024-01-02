from django.contrib import admin
from . models import Category, Customer, Product, Order
from django.db import models
# Register your models here.


admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Order)

