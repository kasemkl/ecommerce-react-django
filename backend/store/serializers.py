from rest_framework import serializers
from .models import *

        
class UserRegisterSerializer(serializers.ModelSerializer):
        class Meta:
            model = Account
            fields = ['username', 'password','email', 'first_name', 'last_name', 'profile_photo']

        def create(self, validated_data):
            try:
                user = Account.objects.create_user(**validated_data)
                return user
            except Exception as e:
                raise ValidationError({'message': str(e)})
class CategoriesSerialzer(serializers.ModelSerializer):
    class Meta:
        model=Categories
        fields='__all__'
        
class ProductSerialzer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'
class OrderSerialzer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields='__all__'
class OrderItemsSerialzer(serializers.ModelSerializer):
    class Meta:
        model=OrderItems
        fields='__all__'