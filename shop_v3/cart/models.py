from django.db import models
from users.models import MyUser
from shop.models import Product


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
		return self.product.name + ' in cart of user ' + self.cart.user.email
