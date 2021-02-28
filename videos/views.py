from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Video


class AllVideosView(ListView):
	"""Предстовление списока всех видео"""
	template_name = 'all_video.html'
	queryset = Video.objects.order_by('-date_creation')
	paginate_by = 6


class OneVideoView(DetailView):
	"""Предстовление одного видео"""
	template_name = 'one_video.html'
	model = Video


class AddVideoView(CreateView):
	"""Предстовление добавления поста с видео"""
	template_name = 'edit_video.html'
	model = Video
	fields = ['slug', 'name', 'body', 'url_video']
	success_url = reverse_lazy('all_videos')


class UpdateVideoView(UpdateView):
	"""Предстовление изменения поста с видео"""
	template_name = 'edit_video.html'
	model = Video
	fields = ['slug', 'name', 'body', 'url_video']
	success_url = reverse_lazy('all_videos')


class DeleteVideoView(DeleteView):
	"""Предстовление удаления поста с видео"""
	template_name = 'delete_video.html'
	model = Video
	success_url = reverse_lazy('all_videos')
