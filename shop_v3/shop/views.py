from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Product, Category
from cart.models import Cart


class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    paginate_by = 18

    def get_queryset(self):
        order = self.request.GET.get('order')
        if order == 'cost_up':
            return Product.objects.order_by('-cost')
        elif order == 'cost_down':
            return Product.objects.order_by('cost')
        else:
            return Product.objects.order_by('name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_list'] = Category.objects.order_by('name')
        if not self.request.user.is_anonymous:
            context['products_in_cart'] = Cart.objects.filter(user=self.request.user, active='t').first().cartitem_set.all().values_list('product', flat=True)

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
        if not self.request.user.is_anonymous:
            context['products_in_cart'] = Cart.objects.filter(user=self.request.user,
                                                          active='t').first().cartitem_set.all().values_list('product',
                                                                                                             flat=True)
        return context


class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        for i in self.get_object().get_reviews().values_list('user', flat=True):
            print(i)

        if self.request.user.id in self.get_object().get_reviews().values_list('user', flat=True):
            context['review_id'] = self.get_object().get_reviews().get(user=self.request.user)
        else:
            context['review_id'] = None
        if not self.request.user.is_anonymous:
            context['products_in_cart'] = Cart.objects.filter(user=self.request.user,
                                                          active='t').first().cartitem_set.all().values_list('product',
                                                                                                             flat=True)
        return context
