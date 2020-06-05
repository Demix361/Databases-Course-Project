from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Cart
from users.models import MyUser


@receiver(post_save, sender=MyUser)
def create_cart(sender, instance, created, **kwargs):
	if created:
		cart = Cart(user=instance)
		cart.save()
		print('CART CREATED AND SAVED')
