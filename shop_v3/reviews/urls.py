from django.urls import path
from .views import ReviewCreateView, ReviewUpdateView, ReviewDeleteView


urlpatterns = [
    path('product/<int:pk>/rev-create/', ReviewCreateView.as_view(), name='review-create'),
    path('product/<int:pk>/<int:rev>/rev-update/', ReviewUpdateView.as_view(), name='review-update'),
    path('product/<int:pk>/<int:rev>/rev-delete/', ReviewDeleteView.as_view(), name='review-delete'),
]