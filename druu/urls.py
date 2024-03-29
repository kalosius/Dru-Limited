from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    # authentication
    path('login/', views.signin, name='login'),
    path('register/', views.registration, name="register"),
    path('update_user/', views.update_user, name="update_user"),
    path('update_info/', views.update_info, name="update_info"),
    path('update_password/', views.update_password, name="update_password"),
    path('logout/', views.logout_user, name="logout"),

    # products
    path('furniture/', views.furniture, name="furniture"),
    path('gadgets/', views.gadgets, name="gadgets"),
    path('pets/', views.pets, name="pets"),
    path('phones&accessories/', views.phones_and_accessories, name="phones&accessories"),
    path('product/<int:pk>', views.product, name="product"),
    path('category/<str:categories>', views.category, name='category'),
    path('category_summary/', views.category_summary, name="category_summary"),
    # path('checkout/', views.checkout, name="checkout"),
    path('search/', views.search, name="search"),
]
