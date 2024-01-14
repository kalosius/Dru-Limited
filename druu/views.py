from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from . models import Product, Category
from cart.cart import Cart
from django.contrib.auth.decorators import login_required


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
    return render(request, 'home.html', {'products':products,})


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
            capitalized_username = username.capitalize()
            messages.success(request, f'Welcome back {capitalized_username}!')
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
    if request.method == 'POST':
        # get form values
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2= request.POST['password2']

        # check if passwords match
        if password1 == password2:
            # check username
            if User.objects.filter(username=username).exists():
                messages.success(request, 'Username already exists')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.success(request, 'Email already exists')
                    return redirect('register')
                else:
                    # looks good
                    capitalized_username = username.capitalize()
                    user = User.objects.create_user(username=username, email=email, password=password1)
                    # login after register
                    auth.login(request, user)
                    messages.success(request, f'Hi {capitalized_username}! Welcome to DruEnterprises...')
                    # return redirect('index')
                    user.save()
                    # messages.success(request, 'You are now registered and can log in')
                    return redirect('home')
        else:
            messages.success(request, 'Passwords do not match')
            return redirect('register')
    else:
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


def checkout(request):
    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quants
    totals = cart.cart_total()

   
    return render(request, 'authentication/checkout.html', {'cart_products':cart_products, 'quantities':quantities, 'totals':totals})