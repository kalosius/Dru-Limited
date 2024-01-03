from . cart import Cart

# creating context processors so cart can work on all pages of the site
def cart(request):
    # returning default data from cart

    return {'cart':Cart(request)}
