from django.urls import path
from .views import CartListView, add_to_cart, remove_from_cart


urlpatterns = [
    path('cart/', CartListView.as_view(), name='cart'),
    path('add-to-cart/<int:pk>/', add_to_cart, name="add-to-cart"),
    path('remove-from-cart/<int:pk>/', remove_from_cart, name="remove-from-cart"),
]
