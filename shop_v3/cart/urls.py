from django.urls import path
from .views import CartListView, add_to_cart, remove_from_cart, increase_quantity, decrease_quantity, OrderCreateView


urlpatterns = [
    path('cart/', CartListView.as_view(), name='cart'),
    path('add-to-cart/<int:pk>/', add_to_cart, name="add-to-cart"),
    path('remove-from-cart/<int:pk>/', remove_from_cart, name="remove-from-cart"),
    path('increase-quantity/<int:pk>/', increase_quantity, name="increase-quantity"),
    path('decrease-quantity/<int:pk>/', decrease_quantity, name="decrease-quantity"),
    path('cart/order/', OrderCreateView.as_view(), name='order-create'),
]
