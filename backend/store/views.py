from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

class UserRegister(APIView):
    
    def post(self,request):
        username = request.data['username']
        email=request.data['email']
        first_name=request.data['first_name']
        last_name=request.data['last_name']
        password=request.data.get('password')
        confirmation_password=request.data.get('confirmation_password')
        if password != confirmation_password:
            return Response({'title':'Failed Registration','message': 'password and confirmation password doesnt match'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            # Use request.FILES for file handling
            image_file = request.FILES.get('profile_photo')
            # Use serializer.validated_data after checking if it's valid
            clean_data = {
                            'username': request.data['username'],
                            'email':request.data['email'],
                            'first_name': request.data['first_name'],
                            'last_name': request.data['last_name'],
                            'password': request.data['password'],
                        }

            serializer = UserRegisterSerializer(data=clean_data)
            if serializer.is_valid():
                instance = serializer.save()
                if image_file:
                    instance.profile_photo = image_file
                    instance.save()
                return Response({'title':'Succesful Registration','message': 'Your Account Created Successfuly'}, status=status.HTTP_201_CREATED)
            else:
                return Response({'message': serializer.errors})
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class CategoriestView(APIView):
    
    def post(self,request):
        name=request.data['name']
        category=Categories.objects.create(name=name)
        
        return Response({'title':'succesful','meassage':'Category added successfully'})
    def get(self,request):
        categories=categories.object.all()
        return Response(categories)

class ProductView(APIView):

    def post(self, request):
        category_id = request.data['category_id']
        name = request.data['name']
        description = request.data['description']
        price = request.data['price']
        quantity = request.data['quantity']

        product = Product.objects.create(
            category_id=category_id,
            name=name,
            description=description,
            price=price,
            quantity=quantity
        )

        images = request.FILES.getlist('images')
        for image in images:
            ProductImages.objects.create(product=product, image=image)

        colors = request.data.getlist('colors')
        for color in colors:
            productColor, created = Colors.objects.get_or_create(color_name=color['name'], color_value=color['value'])
            Products_to_Colors.objects.create(color_id=productColor, product_id=product)

        return Response({'title': 'successful', 'message': 'Product added successfully'})

    def get(self, request):
        products = Product.objects.all()
        products_data = []

        for product in products:
            product_images = ProductImages.objects.filter(product_id=product).first()            
            images = [product_images.image.url] if product_images else []
            product_data = {
                "id":product.id,
                "category_id": product.category_id.id,
                "name": product.name,
                "description": product.description,
                "price": product.price,
                "quantity": product.quantity,
                "images": images,
            }

            products_data.append(product_data)

        return Response(products_data)
    
class SingleProductView(APIView):
    
    def get(self, request, id):
        product = get_object_or_404(Product, id=id)
        images = [image.image.url for image in ProductImages.objects.filter(product_id=product)]
        colors = [{'name': color.color_id.color_name, 'value': color.color_id.color_value} for color in Products_to_Colors.objects.filter(product_id=product)]
        product_data = {
            "category_id": product.category_id.id,
            "name": product.name,
            "description": product.description,
            "price": product.price,
            "quantity": product.quantity,
            "images": images,
            "colors": colors
        }
        return Response({'product': product_data})

class AddToCart(APIView):
    
    def post(self,request,id):
        operation=request.data['operation']
        order=Order.objects.get_or_create(customer=request.user,is_complete=False)
        product=Product.objects.get(id=id)
        if operation=='remove':
            try:
                orderItem=OrderItems.objects.get(product_id=product,order_id=order[0])
                orderItem.quantity-=1
                orderItem.save()
                if orderItem.quantity<=0:
                    orderItem.delete()
                    return Response({'message':'no item'})
                serializers=OrderItemsSerialzer(orderItem)
                return Response({'orderItem':serializers.data})
            except:
                return Response({'message':'no item'})
        orderItem,created=OrderItems.objects.get_or_create(product_id=product,order_id=order[0])
        if not created and operation=='add':
            orderItem.quantity+=1
            orderItem.save()
        serializers=OrderItemsSerialzer(orderItem)
        return Response({'orderitem':serializers.data})
class Cart(APIView):
    
    def get(self,request):
        cart=[]
        order_not_complete=Order.objects.filter(customer=request.user,is_complete=False).first()
        orderItems=OrderItems.objects.all()
        
        for orderItem in orderItems:
            if orderItem.order_id==order_not_complete:
                serializers=OrderItemsSerialzer(cart,many=True)
                cart.append({'quantity':orderItem.quantity,'name': orderItem.product_id.name })
        return Response({'cart':cart})
    