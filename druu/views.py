from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from . models import Product, Category

def category_summary(request):
    categories = Category.objects.all()
    return render(request, 'products/category_summary.html', {"categories":categories})





def product(request,pk):
    product = Product.objects.get(id=pk)
    return render(request, 'products/product.html', {'product':product})

def category(request,categories):
    # categories = categories.replace('-', '') #making the url name with space replaced with a hyphen
    # Grab the category from the url
    try:
        # look up for the category  
        category = Category.objects.get(name=categories)
        products = Product.objects.filter(category=category)
        return render(request, 'products/category.html', {'products':products, 'category':category})

    except: 
        messages.success(request, "Category Doesn't exist...")
        return redirect('home')



def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products':products})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

# for authentication
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # authenticate user
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome Back {username}!')
            return redirect('home')
        else:
            messages.success(request, 'Invalid login credentials')
            return redirect('login')
    return render(request, 'authentication/login.html')

def logout_user(request):
    logout(request)
    messages.success(request, 'You are now logged out!')
    return redirect('home')





def registration(request):
    return render(request, "authentication/register.html")

# Products pages
# def clothes(request):
#     return render(request, 'products/clothes.html')

def furniture(request):
    return render(request, 'products/furniture.html')

def gadgets(request):
    return render(request, 'products/gadgets.html')

def pets(request):
    return render(request, 'products/pets.html')

def phones_and_accessories(request):
    return render(request, 'products/phones.html')



# def sneakers(request):
#     return render(request, 'products/sneakers.html')