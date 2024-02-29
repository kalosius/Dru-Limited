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


# for the above code, sessions weren't working correctly so I had to change it to this:

from druu.models import Product, Profile

class Cart():
    def __init__(self, request):
        self.cart = {}
        self.session = request.session
        # Get request
        self.request = request

        # get current cart from the session
        cart = self.session.get('cart')

        # if the cart is not in the session, create an empty one
        if 'cart' not in request.session:
            cart = self.session['cart'] = {}

        # Make sure cart is available on all pages of the site
        self.cart = cart

    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)

        # if product id is not in cart
        if product_id in self.cart:
            pass
        else:
            # self.cart[product_id] = {'price': str(product.price)}
            self.cart[product_id] = int(product_qty)

        self.session.modified = True

        # Deal with login user
        if self.request.user.is_authenticated:
            # Get the curent user profile
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            #convert {'3':1, '2':4} to {"3":1, "2":4} for JSON
            carty = str(self.cart)
            carty = carty.replace("\'", "\"")
            # Save carty to the profile model
            current_user.update(old_cart=str(carty))

    def __len__(self):
        return len(self.cart)


    def get_prods(self):
        # get ids from cart
        product_ids =   self.cart.keys()
        
        # use ids to look up products in db model
        products = Product.objects.filter(id__in=product_ids)

        # return the looked up products
        return products
    
    def get_quants(self):
        quantities = self.cart
        return quantities
    
    def update(self, product, quantity):
        product_id = str(product)
        product_qty = int(quantity)
        
        # get cart
        mycart = self.cart
        # update dictionary/cart
        mycart[product_id] = product_qty

        self.session.modified = True

        newupdatecart = self.cart
        return newupdatecart 
    
    def delete(self, product):
        product_id = str(product)
        # Delete fro dictionary/cart
        if product_id in self.cart:
            del self.cart[product_id]

        self.session.modified = True



    # cart totals
    def cart_total(self):
        # get product IDs
        product_ids = self.cart.keys()
        # look up those keys in our database model
        products = Product.objects.filter(id__in=product_ids)
        # Get quantities
        quantities = self.cart
        # start counting from zero
        total = 0
        for key, value in quantities.items():
            # Converting key string into integers since its math
            key = int(key)
            for product in products:
                if product.id == key:
                    total = total + (product.price * value)
        return total

        
