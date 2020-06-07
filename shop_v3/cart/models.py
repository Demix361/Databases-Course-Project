from django.db import models
from users.models import MyUser
from shop.models import Product
from django.urls import reverse


class Cart(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    def __str__(self):
        state = 'Не активная'
        if self.active:
            state = 'Активная'
        return f'{state} корзина {self.user.email}'

    def get_cart_items(self):
        return CartItem.objects.filter(cart=self).order_by('product')

    def get_total_no_discount(self):
        total = 0
        for item in self.get_cart_items():
            total += item.quantity * item.product.cost

        return round(total, 2)

    def get_total(self):
        total = 0
        for item in self.get_cart_items():
            total += item.quantity * item.product.cost * (100 - self.user.profile.loyalty_card.discount) / 100

        return round(total, 2)

    def get_item_number(self):
        number = 0
        for item in self.get_cart_items():
            number += item.quantity

        return number

    def is_empty(self):
        if len(self.get_cart_items()) == 0:
            return True
        else:
            return False


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.product.name} in cart id:{self.cart.id} of {self.cart.user.email}'


class Order(models.Model):
    CARD = 'card'
    CASH = 'cash'
    PAYMENT_CHOICES = [
        (CARD, 'Карта'),
        (CASH, 'Наличные')
    ]

    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    amount = models.FloatField()
    order_time = models.DateTimeField(auto_now=True)
    payment_method = models.CharField(
        max_length=4,
        choices=PAYMENT_CHOICES,
        default=CASH
    )
    address = models.CharField(max_length=250, default='')
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Order id: {self.id} of user {self.cart.user.email}'

    def get_absolute_url(self):
        return reverse('shop-home')

    def get_ru_payment(self):
        name_ru = ''
        if self.payment_method == 'card':
            name_ru = 'Картой'
        elif self.payment_method == 'cash':
            name_ru = 'Наличными'

        return name_ru
