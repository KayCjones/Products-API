from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializer import ProductSerializer

# Create your views here.

@api_view(['GET'])
def product_list (request):
    product = Product.objects.all()
    
