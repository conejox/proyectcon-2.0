from django.urls import path
from . import views
#from .views import ProductListCreateView




#urlpatterns = [
 #   path('api/products/', ProductListCreateView.as_view(), name='product-list'),
#]


urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('create/', views.product_create, name='product_create'),
    path('<int:pk>/update/', views.product_update, name='product_update'),
    path('<int:pk>/delete/', views.product_delete, name='product_delete'),
]
