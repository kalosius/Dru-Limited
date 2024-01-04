# from druu.models import Product

# class Cart():
#     def __init__(self, request):
#         self.cart = {}
#         self.session = request.session

#         # get current session key if it exists
#         cart = self.session.get('session_key')

#         # if the user is new no session key! create one!
#         if 'session_key' not in request.session:
#             cart = self.session['session_key'] = {}
        
#         # Make sure cart is available on all pages of the site
#             self.cart = cart

#     def add(self, product):
#         product_id = str(product.id)

#         # if product id is not in cart
#         if product_id in self.cart:
#             pass
#         else:
#             self.cart[product_id] = {'price': str(product.price)}

#         self.session.modified = True

#     def __len__(self):
#         return len(self.cart)

from druu.models import Product

class Cart():
    def __init__(self, request):
        self.cart = {}
        self.session = request.session

        # get current cart from the session
        cart = self.session.get('cart')

        # if the cart is not in the session, create an empty one
        if 'cart' not in request.session:
            cart = self.session['cart'] = {}

        # Make sure cart is available on all pages of the site
        self.cart = cart

    def add(self, product):
        product_id = str(product.id)

        # if product id is not in cart
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = {'price': str(product.price)}

        self.session.modified = True

    def __len__(self):
        return len(self.cart)
