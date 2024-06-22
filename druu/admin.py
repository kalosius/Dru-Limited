from django.contrib import admin
from .models import Category, Customer, Product, Order, Profile
from django.contrib.auth.models import User

admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Profile)

# mixing profile and user info

class ProfileInline(admin.StackedInline):
    model = Profile
    # extend the user model
class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username", "first_name", "last_name", "email"]
    inlines = [ProfileInline]
# unregister
admin.site.unregister(User)
    
# re-registering the new profile
admin.site.register(User, UserAdmin)