from django.urls import path
from .views import *
urlpatterns = [
    path('products/',ProductView.as_view()),
    path('products/<int:id>/',SingleProductView.as_view()),
    path('cart/<int:id>/',AddToCart.as_view()),
    path('cart/',Cart.as_view()),
    
]