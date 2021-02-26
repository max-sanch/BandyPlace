from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Product


class AllProductsView(ListView):
	"""Предстовление списока всех продуктов"""
	template_name = 'all_prods.html'
	model = Product
	paginate_by = 6


class AddProductView(CreateView):
	"""Предстовление добавления продукта"""
	template_name = 'edit_prod.html'
	model = Product
	fields = ['slug', 'name', 'description', 'image', 'url_shop', 'price']


class UpdateProductView(UpdateView):
	"""Предстовление изменения продукта"""
	template_name = 'edit_prod.html'
	model = Product
	fields = ['slug', 'name', 'description', 'image', 'url_shop', 'price']


class DeleteProductView(DeleteView):
	"""Предстовление удаления продукта"""
	model = Product
	success_url = '/all_prods/'
