from django.db import models
from users.models import MyUser
from shop.models import Product
from django.urls import reverse


class Cart(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    # total_cost = models.FloatField()

    def __str__(self):
        return f'Cart id: {self.id} of user {self.user.email}'


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
