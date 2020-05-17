from django.urls import path
from .views import ProductListView, ProductDetailView


urlpatterns = [
    path('', ProductListView.as_view(), name='shop-home'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='shop-product')
]
