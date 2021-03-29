from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import UpcomingGame


class UpcomingGameView(ListView):
	"""Предстовление списока всех предстоящих игр"""
	template_name = 'all_new_games.html'
	queryset = UpcomingGame.objects.order_by('date', 'time')
	paginate_by = 8


class AddUpcomingGameView(CreateView):
	"""Предстовление добавления предстоящих игр"""
	template_name = 'edit_new_game.html'
	model = UpcomingGame
	fields = ['team_one', 'team_two', 'date', 'time', 'address']
	success_url = reverse_lazy('add_new_game')


class UpdateUpcomingGameView(UpdateView):
	"""Предстовление изменения предстоящих игр"""
	template_name = 'edit_new_game.html'
	model = UpcomingGame
	fields = ['team_one', 'team_two', 'date', 'address']
	success_url = reverse_lazy('all_new_games')


class DeleteUpcomingGameView(DeleteView):
	"""Предстовление удаления предстоящих игр"""
	model = UpcomingGame
	success_url = reverse_lazy('all_new_games')
