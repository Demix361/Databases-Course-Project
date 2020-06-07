from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.utils.decorators import method_decorator
from .models import Cart, CartItem, Order
from users.models import MyUser, LoyaltyCard
from shop.models import Product


class CartListView(LoginRequiredMixin, ListView):
    model = Cart
    template_name = 'cart/cart_list.html'
    context_object_name = 'cart'

    def get_queryset(self):
        return Cart.objects.get(user=self.request.user, active='t')


class OrderDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Order
    template_name = 'cart/order_detail.html'
    context_object_name = 'order'

    def test_func(self):
        order = self.get_object()
        if self.request.user == order.cart.user:
            return True
        return False


class OrderCreateView(LoginRequiredMixin, CreateView):
    model = Order
    fields = ['payment_method', 'address', 'notes']

    def form_valid(self, form):
        user = self.request.user
        cart_items = Cart.objects.filter(user=user, active='t').first().cartitem_set.all()

        form.instance.cart = Cart.objects.get(user=user, active='t')
        total = 0
        for item in cart_items:
            total += Product.objects.get(id=item.product.id).cost * item.quantity
        if user.profile.loyalty_card:
            total *= (100 - user.profile.loyalty_card.discount) / 100
        if total == 0:
            total = None
        form.instance.amount = total

        # disable current cart and add new
        Cart.objects.filter(user=user, active='t').update(active='f')
        new_cart = Cart(user=user)
        new_cart.save()

        # update loyalty card if needed
        money_sum = 0
        for obj in Cart.objects.filter(user=user):
            ord = Order.objects.filter(cart=obj).first()
            if ord:
                money_sum += ord.amount           
        money_sum += total

        cur_cart = user.profile.loyalty_card.name
        if cur_cart != 'Алмазный':
            if cur_cart == 'Отсутствует':
                next_cart = 'Бронзовый'
                limit = 10000
            elif cur_cart == 'Бронзовый':
                next_cart = 'Серебряный'
                limit = 40000
            elif cur_cart == 'Серебряный':
                next_cart = 'Золотой'
                limit = 70000
            elif cur_cart == 'Золотой':
                next_cart = 'Платиновый'
                limit = 150000
            elif cur_cart == 'Платиновый':
                next_cart = 'Алмазный'
                limit = 300000
            print()
            print(cur_cart)
            print(next_cart)
            print(limit)
            print(money_sum)
            print()
            if money_sum > limit:
                user.profile.loyalty_card = LoyaltyCard.objects.get(name=next_cart)
                user.profile.save()

        return super().form_valid(form)


class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'cart/order_list.html'
    context_object_name = 'orders'
    paginate_by = 12

    def get_queryset(self):
        return Order.objects.filter(cart__user=self.request.user).order_by('-order_time')


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
