from django.urls import path
from .views import *
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

urlpatterns = [
    path('',IndexView.as_view(),name='index'),
    path('blog/',BlogView.as_view(),name='blog'),
    path('blog-1/',Blog1View.as_view(),name='blog-1'),
    path('blog-2/',Blog2View.as_view(),name='blog-2'),
    path('blog-3/',Blog3View.as_view(),name='blog-3'),
    path('blog-single/',BlogSingleView.as_view(),name='blog-single'),
    path('shop-single/',ShopSingleView.as_view(),name='shop-single'),
    path('shop-cart/',ShopCartView.as_view(),name='shop-cart'),

    ]