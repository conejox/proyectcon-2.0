from django.shortcuts import render
from .models import Product
from rest_framework import generics
from .serializers import ProductSerializer
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProductForm





class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



# List
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

# Create
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'products/product_form.html', {'form': form})

# Update
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'products/product_form.html', {'form': form})

# Delete
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'products/product_confirm_delete.html', {'product': product})
