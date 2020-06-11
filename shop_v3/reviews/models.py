from django.db import models
from django.conf import settings


class Review(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	product = models.ForeignKey('shop.Product', on_delete=models.CASCADE)
	rating = models.IntegerField()
	advantages = models.TextField()
	disadvantages = models.TextField()
	review = models.TextField()
	date_posted = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f'Отзыв {self.user.email} о {self.product.name}'
