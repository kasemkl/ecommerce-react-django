from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Account)
admin.site.register(Categories)
admin.site.register(Product)
admin.site.register(Colors)
admin.site.register(ProductImages)
admin.site.register(Products_to_Colors)
admin.site.register(Order)
admin.site.register(OrderItems)