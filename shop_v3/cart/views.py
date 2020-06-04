from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Cart, CartItem
from users.models import MyUser
from shop.models import Product


class CartListView(ListView):
    model = Cart
    context_object_name = 'carts'
    # paginate_by = 18

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CartListView, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user, active='t')


@login_required()
def add_to_cart(request, **kwargs):
    product = Product.objects.filter(id=kwargs.get('pk')).first()
    user = request.user
    cart = Cart.objects.filter(user=user, active='t').first()
    new_cart_item = CartItem(cart=cart, product=product)
    new_cart_item.save()

    print('=' * 50)
    print(product.name)
    print(user.email)
    print(cart)

    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
