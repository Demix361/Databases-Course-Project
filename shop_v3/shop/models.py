from django.db import models
from django.contrib.postgres.fields import ArrayField


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    color = models.CharField(max_length=50)
    cost = models.FloatField()
    description = models.TextField()
    image = models.ImageField(default='product_default.jpg', upload_to='product_pics')

    def __str__(self):
        return self.name
