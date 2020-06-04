from django.urls import path
from .views import ProductListView, ProductDetailView, ProductCategoryListView


urlpatterns = [
    path('', ProductListView.as_view(), name='shop-home'),
    path('category/<str:category>/', ProductCategoryListView.as_view(), name='shop-category'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='shop-product')
]
