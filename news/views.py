from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Post


class AllPostsView(ListView):
	"""Предстовление списока всех постов"""
	template_name = 'all_posts.html'
	model = Post
	paginate_by = 6


class OnePostView(DetailView):
	"""Предстовление одного новостного поста"""
	template_name = 'one_post.html'
	model = Post


class AddPostView(CreateView):
	"""Предстовление добавления новостного поста"""
	template_name = 'edit_post.html'
	model = Post
	fields = ['slug', 'title', 'body', 'image']


class UpdatePostView(UpdateView):
	"""Предстовление изменения новостного поста"""
	template_name = 'edit_post.html'
	model = Post
	fields = ['slug', 'title', 'body', 'image']


class DeletePostView(DeleteView):
	"""Предстовление удаления новостного поста"""
	model = Post
	success_url = '/all_posts/'
