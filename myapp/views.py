from django.shortcuts import render
from django.views.generic import TemplateView




class IndexView(TemplateView):
	template_name = 'index.html'

class BlogView(TemplateView):
	template_name = 'blog.html'

class ShopSingleView(TemplateView):
	template_name = 'shop-single.html'

class Blog1View(TemplateView):
	template_name = 'blog-1.html'

class Blog2View(TemplateView):
	template_name = 'blog-2.html'

class Blog3View(TemplateView):
	template_name = 'blog-3.html'

class BlogSingleView(TemplateView):
	template_name = 'blog-single.html'

class ShopCartView(TemplateView):
	template_name = 'shop-cart.html'

