from django.urls import reverse_lazy
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
	success_url = reverse_lazy('add_prod')


class UpdateProductView(UpdateView):
	"""Предстовление изменения продукта"""
	template_name = 'edit_prod.html'
	model = Product
	fields = ['slug', 'name', 'description', 'image', 'url_shop', 'price']
	success_url = reverse_lazy('all_prods')


class DeleteProductView(DeleteView):
	"""Предстовление удаления продукта"""
	template_name = 'delete_prod.html'
	model = Product
	success_url = reverse_lazy('all_prods')
