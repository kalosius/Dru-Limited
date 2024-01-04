# views.py
from django.shortcuts import render, get_object_or_404
from .cart import Cart
from druu.models import Product
from django.http import JsonResponse
from django.http import HttpResponse

# Create your views here.

def cart_summary(request):
    # Get the cart
    cart = Cart(request)
    cart_products = cart.get_prods

    return render(request, 'cart_summary.html', {'cart_products':cart_products})

def cart_add(request):
    # get the cart
    cart = Cart(request)

    # test for POST
    if request.POST.get('action') == 'post':
        # get stuff
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        # lookup product in the DB
        product = get_object_or_404(Product, id=product_id)

        # save to session
        cart.add(product, quantity=product_qty)


        # get cart quantity
        cart_quantity = cart.__len__()

        # return a JSON response
        # response = JsonResponse({'Product Name': product.name})
        response = JsonResponse({'qty': cart_quantity})

        return response


def cart_delete(request):
    pass

def cart_update(request):
    pass

