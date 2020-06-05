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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        cart_items = Cart.objects.filter(user=user, active='t').first().cartitem_set.all()

        context['item_quantity'] = sum([i for i in Cart.objects.filter(user=user, active='t').first().cartitem_set.all().values_list('quantity', flat=True)])
        context['total_cost'] = 0
        for item in cart_items:
            context['total_cost'] += Product.objects.get(id=item.product.id).cost * item.quantity
        if user.profile.loyalty_card:
            context['total_cost'] = context['total_cost'] * (100 - user.profile.loyalty_card.discount) / 100

        return context


@login_required()
def add_to_cart(request, **kwargs):
    product = Product.objects.filter(id=kwargs.get('pk')).first()
    user = request.user
    cart = Cart.objects.filter(user=user, active='t').first()

    if product.id not in Cart.objects.filter(user=user, active='t').first().cartitem_set.all().values_list('product', flat=True):
        new_cart_item = CartItem(cart=cart, product=product)
        new_cart_item.save()

        print('ITEM ADDED TO CART')
    else:
        print('ITEM ALREADY IN CART')

    return redirect(request.META.get('HTTP_REFERER', 'shop-home'))


@login_required()
def remove_from_cart(request, **kwargs):
    product = Product.objects.filter(id=kwargs.get('pk')).first()
    user = request.user
    cart = Cart.objects.filter(user=user, active='t').first()

    if product.id in Cart.objects.filter(user=user, active='t').first().cartitem_set.all().values_list('product', flat=True):
        CartItem.objects.filter(cart=cart, product=product).delete()

        print('ITEM DELETED')
    else:
        print('ITEM NOT IN CART')

    return redirect(request.META.get('HTTP_REFERER', 'shop-home'))


@login_required()
def increase_quantity(request, **kwargs):
    product = Product.objects.filter(id=kwargs.get('pk')).first()
    user = request.user
    cart = Cart.objects.filter(user=user, active='t').first()

    if product.id in Cart.objects.filter(user=user, active='t').first().cartitem_set.all().values_list('product', flat=True):
        quantity = CartItem.objects.filter(cart=cart, product=product).first().quantity

        if quantity < 20:
            CartItem.objects.filter(cart=cart, product=product).update(quantity=quantity + 1)
            print('ITEM QUANTITY INCREASED')
        else:
            print('MAXIMUM QUANTITY IS REACHED')
    else:
        print('ITEM NOT IN CART')

    return redirect(request.META.get('HTTP_REFERER', 'shop-home'))


@login_required()
def decrease_quantity(request, **kwargs):
    product = Product.objects.filter(id=kwargs.get('pk')).first()
    user = request.user
    cart = Cart.objects.filter(user=user, active='t').first()

    if product.id in Cart.objects.filter(user=user, active='t').first().cartitem_set.all().values_list('product', flat=True):
        quantity = CartItem.objects.filter(cart=cart, product=product).first().quantity

        if quantity > 1:
            CartItem.objects.filter(cart=cart, product=product).update(quantity=quantity - 1)
            print('ITEM QUANTITY DECREASED')
        else:
            print('MINIMUM QUANTITY IS REACHED')
    else:
        print('ITEM NOT IN CART')

    return redirect(request.META.get('HTTP_REFERER', 'shop-home'))
