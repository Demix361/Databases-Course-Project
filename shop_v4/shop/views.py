from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.db.models import Q
from .models import Product, Category, Feature, FeatureVariant, FeatureSet
from cart.models import Cart
from functools import reduce


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
            context['products_in_cart'] = Cart.objects.filter(user=self.request.user).first().cartitem_set.all().values_list('product', flat=True)

        return context


def is_valid_queryparam(param):
    return param != '' and param is not None


def filter_products(options, category_id):
    q_or = reduce(lambda q, f: q | Q(feature_variant=f), options[0], Q())
    q_and = reduce(lambda q, f: q & Q(feature_variant=f), options[1], Q())
    print(q_or)
    print(q_and)
    #res = FeatureSet.objects.filter(Q(product.category.id = category_id) & q_or & q_and)
    res = FeatureSet.objects.filter(q_or & q_and)
    for i in res:
        print(i.product.name)


class ProductCategoryDetailView(DetailView):
    model = Category
    template_name = 'shop/productcategory_list.html'
    context_object_name = 'category'
    paginate_by = 18

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        var_1 = self.request.GET.get('var_1')
        if is_valid_queryparam(var_1):
            print(var_1)

        if not self.request.user.is_anonymous:
            context['products_in_cart'] = Cart.objects.filter(
                user=self.request.user).first().cartitem_set.all().values_list('product',
                                                                                       flat=True)

        context['filtered_products'] = Product.objects.filter(category=self.get_object())
        res = FeatureSet

        all_q = self.get_object().get_products()
        max_len = len(all_q)
        filters_id = [[], []]
        for f in self.get_object().get_features():
            if f.type == 'checkbox':
                for v in f.get_variants():
                    var = self.request.GET.get('ch_' + str(v.id))

                    if is_valid_queryparam(var):
                        filters_id[0].append(v.id)


            elif f.type == 'radiobutton':
                var = self.request.GET.get('rb_' + str(f.id))

                if is_valid_queryparam(var) and var != 'no':
                    try:
                        var = int(var)
                        filters_id[1].append(var)
                        res = res.objects.filter(feature_variant=var)
                    except ValueError:
                        pass

        print(filters_id)

        for filter in filters_id[0]:
            

        #filter_products(filters_id, self.get_object().id)

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
            context['products_in_cart'] = Cart.objects.filter(user=self.request.user).first().cartitem_set.all().values_list('product',
                                                                                                             flat=True)
        return context
