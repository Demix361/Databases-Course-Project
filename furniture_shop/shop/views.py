from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product


class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    paginate_by = 18

class ProductDetailView(DetailView):
    model = Product
