from django.urls import path
from .views import ProductListView, ProductDetailView, ProductCategoryListView
# from django.urls.converters import register_converter
# from transliterate import translit, get_available_language_codes

'''
class MyConverter:
    regex = '[^/]+'

    def to_python(self, value):
        return value

    def to_url(self, value):
        return translit(str(value), 'ru', reversed=True).lower()


register_converter(MyConverter, 'my_str')
'''

urlpatterns = [
    path('', ProductListView.as_view(), name='shop-home'),
    path('category/<str:category>/', ProductCategoryListView.as_view(), name='shop-category'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='shop-product')
]
