from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.utils.decorators import method_decorator
from .models import Cart, CartItem, Order, OrderItem
from users.models import MyUser, LoyaltyCard
from shop.models import Product


# OK
class CartListView(LoginRequiredMixin, ListView):
    model = Cart
    template_name = 'cart/cart_list.html'
    context_object_name = 'cart'

    def get_queryset(self):
        return Cart.objects.get(user=self.request.user)


#!!!!!!!!!!!
class OrderDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Order
    template_name = 'cart/order_detail.html'
    context_object_name = 'order'

    def test_func(self):
        order = self.get_object()
        if self.request.user == order.user:
            return True
        return False


# OK
class OrderCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Order
    fields = ['payment_method', 'address', 'notes']

    def form_valid(self, form):
        '''
        user = self.request.user
        cart = Cart.objects.get(user=user, active='t')

        form.instance.cart = cart
        form.instance.amount = cart.get_total()

        # upgrade loyalty card if needed
        user.profile.upgrade_loyalty_card()

        # disable current cart and add new
        cart.active = 'f'
        cart.save()
        new_cart = Cart(user=user)
        new_cart.save()
        '''
        user = self.request.user
        form.instance.user = user

        # Перемещение и удаление товаров из корзины в сигналах
        return super().form_valid(form)

    def test_func(self):
        user = self.request.user
        if Cart.objects.get(user=user).is_empty():  # Проверить!
            return False
        return True


# OK
class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'cart/order_list.html'
    context_object_name = 'orders'
    paginate_by = 12

    def get_queryset(self):
        #return Order.objects.filter(cart__user=self.request.user).order_by('-order_time')
        return Order.objects.filter(user=self.request.user).order_by('-order_time')


# OK
@login_required()
def add_to_cart(request, **kwargs):
    product = Product.objects.filter(id=kwargs.get('pk')).first()
    cart = Cart.objects.get(user=request.user)

    if product.id not in cart.cartitem_set.all().values_list('product', flat=True):
        new_cart_item = CartItem(cart=cart, product=product)
        new_cart_item.save()
        print('ITEM ADDED TO CART')
    else:
        print('ITEM ALREADY IN CART')

    #if product.id not in Cart.objects.filter(user=user, active='t').first().cartitem_set.all().values_list('product', flat=True):
    #    new_cart_item = CartItem(cart=cart, product=product)
    #    new_cart_item.save()

    #    print('ITEM ADDED TO CART')
    #else:
    #    print('ITEM ALREADY IN CART')

    return redirect(request.META.get('HTTP_REFERER', 'shop-home'))


# OK?
@login_required()
def remove_from_cart(request, **kwargs):
    product = Product.objects.filter(id=kwargs.get('pk')).first()
    cart = Cart.objects.get(user=request.user)
    #cart = Cart.objects.filter(user=user, active='t').first()

    #if product.id in Cart.objects.filter(user=user, active='t').first().cartitem_set.all().values_list('product', flat=True):
    #    CartItem.objects.filter(cart=cart, product=product).delete()

    #    print('ITEM DELETED')
    #else:
    #    print('ITEM NOT IN CART')

    if product.id in cart.cartitem_set.all().values_list('product', flat=True):
        CartItem.objects.filter(cart=cart, product=product).delete()
        print('ITEM DELETED')
    else:
        print('ITEM NOT IN CART')

    return redirect(request.META.get('HTTP_REFERER', 'shop-home'))


# OK?
@login_required()
def increase_quantity(request, **kwargs):
    product = Product.objects.filter(id=kwargs.get('pk')).first()
    cart = Cart.objects.get(user=request.user)
    #cart = Cart.objects.filter(user=user, active='t').first()

    #if product.id in Cart.objects.filter(user=user, active='t').first().cartitem_set.all().values_list('product', flat=True):
    #    quantity = CartItem.objects.filter(cart=cart, product=product).first().quantity

    #    if quantity < 20:
    #        CartItem.objects.filter(cart=cart, product=product).update(quantity=quantity + 1)
    #        print('ITEM QUANTITY INCREASED')
    #    else:
    #        print('MAXIMUM QUANTITY IS REACHED')
    #else:
    #    print('ITEM NOT IN CART')

    if product.id in cart.cartitem_set.all().values_list('product', flat=True):
        quantity = CartItem.objects.filter(cart=cart, product=product).first().quantity

        if quantity < 20:
            CartItem.objects.filter(cart=cart, product=product).update(quantity=quantity + 1)
            print('ITEM QUANTITY INCREASED')
        else:
            print('MAXIMUM QUANTITY IS REACHED')
    else:
        print('ITEM NOT IN CART')


    return redirect(request.META.get('HTTP_REFERER', 'shop-home'))


# OK?
@login_required()
def decrease_quantity(request, **kwargs):
    product = Product.objects.filter(id=kwargs.get('pk')).first()
    cart = Cart.objects.get(user=request.user)
    #cart = Cart.objects.filter(user=user, active='t').first()

    #if product.id in Cart.objects.filter(user=user, active='t').first().cartitem_set.all().values_list('product', flat=True):
    #    quantity = CartItem.objects.filter(cart=cart, product=product).first().quantity

    #    if quantity > 1:
    #        CartItem.objects.filter(cart=cart, product=product).update(quantity=quantity - 1)
    #        print('ITEM QUANTITY DECREASED')
    #    else:
    #        print('MINIMUM QUANTITY IS REACHED')
    #else:
    #    print('ITEM NOT IN CART')

    if product.id in cart.cartitem_set.all().values_list('product', flat=True):
        quantity = CartItem.objects.filter(cart=cart, product=product).first().quantity

        if quantity > 1:
            CartItem.objects.filter(cart=cart, product=product).update(quantity=quantity - 1)
            print('ITEM QUANTITY DECREASED')
        else:
            print('MINIMUM QUANTITY IS REACHED')
    else:
        print('ITEM NOT IN CART')

    return redirect(request.META.get('HTTP_REFERER', 'shop-home'))
