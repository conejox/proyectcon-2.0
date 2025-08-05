from django.shortcuts import render
from .models import Product
from rest_framework import generics
from .serializers import ProductSerializer

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})



class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
