from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin,Group
from django.core.validators import MaxValueValidator,MinValueValidator


class AppUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        # Create and save a regular user
        if not username:
            raise ValueError('username is required.')

        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        # Create and save a superuser
        user = self.create_user(username, password,type='admin', **extra_fields)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
        new_group1, created = Group.objects.get_or_create(name='customer')
        new_group2, created = Group.objects.get_or_create(name='admin')
        user.groups.add(new_group2)
        return user

class Account(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=20,unique=True)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)   
    last_name = models.CharField(max_length=255)
    type = models.CharField(max_length=255, default='customer')
    profile_photo = models.ImageField(upload_to='images/', default='../media/images/default_profile_photo.jpg')
    email=models.EmailField()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name','email']

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = AppUserManager()
    
    def __str__(self):
        return str(self.username)
    
class Categories(models.Model):
    name=models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.name
    
class Product(models.Model):
    category_id=models.ForeignKey(Categories,on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity=models.IntegerField()
    
    def __str__(self):
        return self.name

class ProductImages(models.Model):
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='products/')
    
class Ratings(models.Model):
    product_id=models.OneToOneField(Product,on_delete=models.CASCADE)
    rating = models.FloatField(validators=[MaxValueValidator(10), MinValueValidator(0)])
    message=models.CharField(max_length=255)
    
class Colors(models.Model):
    color_name=models.CharField(max_length=255)
    color_value=models.CharField(max_length=255)

class Products_to_Colors(models.Model):
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE)
    color_id=models.ForeignKey(Colors,on_delete=models.CASCADE)

class Order(models.Model):
    customer=models.ForeignKey(Account,on_delete=models.CASCADE)
    city=models.CharField(max_length=255)
    street_address=models.CharField(max_length=255)
    appartment=models.CharField(max_length=255)
    phone=models.CharField(max_length=15)
    payment_method=models.CharField(max_length=255)
    is_complete=models.BooleanField(default=False)

class OrderItems(models.Model):
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    order_id=models.ForeignKey(Order,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.product_id.name
    
    def total(self):
        return self.quantity*self.product_id.price

class WishList(models.Model):
    customer=models.ForeignKey(Account,on_delete=models.CASCADE)
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE)
    
