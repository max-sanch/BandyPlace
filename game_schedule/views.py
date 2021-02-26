from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import UpcomingGame


class UpcomingGameView(ListView):
	"""Предстовление списока всех предстоящих игр"""
	template_name = 'all_new_games.html'
	model = UpcomingGame
	paginate_by = 6


class AddUpcomingGameView(CreateView):
	"""Предстовление добавления предстоящих игр"""
	template_name = 'edit_new_game.html'
	model = UpcomingGame
	fields = ['team_one', 'team_two', 'date', 'address']


class UpdateUpcomingGameView(UpdateView):
	"""Предстовление изменения предстоящих игр"""
	template_name = 'edit_new_game.html'
	model = UpcomingGame
	fields = ['team_one', 'team_two', 'date', 'address']


class DeleteUpcomingGameView(DeleteView):
	"""Предстовление удаления предстоящих игр"""
	model = UpcomingGame
	success_url = '/'
