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
        return Cart.objects.filter(user=self.request.user)


@login_required()
def add_to_cart(request, **kwargs):
    # get the user profile
    user = get_object_or_404(MyUser, profile=request.profile)

    print('=' * 50)
    print(user)

    # filter products by id
    #product = Product.objects.filter(id=kwargs.get('item_id', "")).first()


    # card_item = CartItem.objects.create(cart=, is_ordered=False)


    # show confirmation message and redirect back to the same page
    #return redirect(reverse('products:product-list'))
