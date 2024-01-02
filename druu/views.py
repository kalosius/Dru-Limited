from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

# for authentication
def signin(request):
    return render(request, 'authentication/login.html')


def registration(request):
    return render(request, "authentication/register.html")

# Products pages
def clothes(request):
    return render(request, 'products/clothes.html')

def furniture(request):
    return render(request, 'products/furniture.html')

def gadgets(request):
    return render(request, 'products/gadgets.html')

def pets(request):
    return render(request, 'products/pets.html')

def phones_and_accessories(request):
    return render(request, 'products/phones.html')

def sneakers(request):
    return render(request, 'products/sneakers.html')