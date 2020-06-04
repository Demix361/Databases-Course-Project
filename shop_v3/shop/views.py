from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Product, Category


class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    paginate_by = 18

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_list'] = Category.objects.order_by('name')
        return context


class ProductCategoryListView(ListView):
    model = Product
    template_name = 'shop/productcategory_list.html'
    context_object_name = 'products'
    paginate_by = 18

    def get_queryset(self):
        category = get_object_or_404(Category, name=self.kwargs.get('category'))
        return Product.objects.filter(category=category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_list'] = Category.objects.order_by('name')
        return context


class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_list'] = Category.objects.order_by('name')
        return context
