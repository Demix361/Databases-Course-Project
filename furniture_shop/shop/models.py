from django.db import models
from django.contrib.postgres.fields import ArrayField


class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    cost = models.FloatField()
    description = models.TextField()
    images = models.ImageField(default='product_default.jpg', upload_to='product_pics')

    def __str__(self):
        return self.name
