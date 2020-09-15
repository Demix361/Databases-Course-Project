from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.db.models import Q
from .models import Product, Category, Feature, FeatureVariant, FeatureSet, Color
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


class ProductCategoryDetailView(DetailView):
    model = Category
    template_name = 'shop/productcategory_list.html'
    context_object_name = 'category'
    paginate_by = 18

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Список товаров в корзине
        if not self.request.user.is_anonymous:
            context['products_in_cart'] = Cart.objects.filter(
                user=self.request.user).first().cartitem_set.all().values_list('product', flat=True)

        # Список цветов
        context['colors'] = Color.objects.all()

        filtered_q = FeatureSet.objects.filter(product__category=self.get_object(), product__displayed=True)

        # radiobutton Наличие
        var = self.request.GET.get('rb_st')
        if is_valid_queryparam(var):
            if var == 'yes':
                filtered_q = FeatureSet.objects.filter(product__category=self.get_object(), product__displayed=True, product__in_stock=True)
            elif var == 'no':
                filtered_q = FeatureSet.objects.filter(product__category=self.get_object(), product__displayed=True, product__in_stock=False)

        # Если категория имеет features
        if len(filtered_q) != 0:

            # CHECKBOX
            used = []
            for f in self.get_object().get_features().filter(type='checkbox'):
                cur_filtered = FeatureSet.objects.none()
                used.append([])
                for v in f.get_variants():
                    var = self.request.GET.get('ch_' + str(v.id))

                    if is_valid_queryparam(var):
                        used[-1].append(1)
                        for line in FeatureSet.objects.filter(feature_variant=v.id):
                            cur_filtered = cur_filtered | FeatureSet.objects.filter(product=line.product)
                    else:
                        used[-1].append(0)
                # Если хотя бы один чекбокс в фильтре был отмечен, используем AND с прошлым результатом
                if 1 in used[-1]:
                    filtered_q = filtered_q & cur_filtered

            # RADIOBUTTON
            for f in self.get_object().get_features().filter(type='radiobutton'):
                var = self.request.GET.get('rb_' + str(f.id))

                if is_valid_queryparam(var) and var != 'no':
                    cur_filtered = FeatureSet.objects.none()

                    for line in FeatureSet.objects.filter(feature_variant=int(var)):
                        cur_filtered = cur_filtered | FeatureSet.objects.filter(product=line.product)

                    filtered_q = filtered_q & cur_filtered

            # COLOR
            cur_filtered = FeatureSet.objects.none()
            used = []
            for clr in Color.objects.all():
                var = self.request.GET.get('clr_' + str(clr.id))

                if is_valid_queryparam(var):
                    used.append(1)
                    for line in FeatureSet.objects.filter(product__color=clr.id):
                        cur_filtered = cur_filtered | FeatureSet.objects.filter(product=line.product)
                else:
                    used.append(0)

            if 1 in used:
                filtered_q = filtered_q & cur_filtered

            # FeatureSet -> Product
            ok_products = []
            for p in filtered_q.values('product'):
                ok_products.append(p['product'])
            ok_products = set(ok_products)

            final_products = Product.objects.none()
            for i in ok_products:
                if i in filtered_q.values('product'):
                    print(i, 'ok')
                final_products = final_products | Product.objects.filter(id=i)

            context['filtered_products'] = final_products
        # Если продукт не имеет features
        else:
            used = []
            cur_products = Product.objects.none()

            for clr in Color.objects.all():
                var = self.request.GET.get('clr_' + str(clr.id))

                if is_valid_queryparam(var):
                    used.append(1)
                    cur_products = cur_products | Product.objects.filter(color=clr.id)
                else:
                    used.append(0)

            if 1 in used:
                context['filtered_products'] = cur_products
            else:
                context['filtered_products'] = self.get_object().get_products()

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
        context['product_features'] = FeatureSet.objects.filter(product=self.get_object())
        return context
