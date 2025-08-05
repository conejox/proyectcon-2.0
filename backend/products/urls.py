from django.urls import path
from . import views
from .views import ProductListCreateView

urlpatterns = [
    path('products/', views.product_list, name='product_list'),
]



urlpatterns = [
    path('api/products/', ProductListCreateView.as_view(), name='product-list'),
]
