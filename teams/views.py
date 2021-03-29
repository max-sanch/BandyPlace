from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Team, TeamStat, Player, PlayerStat, PastGame, PastGameStat


# Команды
class StatTeamsView(TemplateView):
	"""Предстовление статистики команд"""
	template_name = 'stat_teams.html'


class AddStatTeamView(CreateView):
	"""Предстовление добавления статистики команды"""
	template_name = 'edit_stat_team.html'
	model = TeamStat
	fields = ['team']


class UpdateStatTeamView(UpdateView):
	"""Предстовление изменения статистики команды"""
	template_name = 'edit_stat_team.html'
	model = TeamStat
	fields = ['team']
	success_url = reverse_lazy('stat_teams')


class DeleteStatTeamView(DeleteView):
	"""Предстовление удаления статистики команды"""
	template_name = 'delete_stat_team.html'
	model = TeamStat
	success_url = '/stat_teams/'


class AddTeamView(CreateView):
	"""Предстовление добавления команды"""
	template_name = 'edit_team.html'
	model = Team
	fields = ['name', 'logo']
	success_url = reverse_lazy('add_team')


class UpdateTeamView(UpdateView):
	"""Предстовление изменения команды"""
	template_name = 'edit_team.html'
	model = Team
	fields = ['name', 'logo']
	success_url = reverse_lazy('stat_teams')


class DeleteTeamView(DeleteView):
	"""Предстовление удаления команды"""
	template_name = 'delete_team.html'
	model = Team
	success_url = reverse_lazy('stat_teams')


# Игроки
class StatPlayersView(TemplateView):
	"""Предстовление статистики игрока"""
	template_name = 'stat_players.html'


class AddStatPlayerView(CreateView):
	"""Предстовление добавления статистики игрока"""
	template_name = 'edit_stat_player.html'
	model = PlayerStat
	fields = ['player']


class UpdateStatPlayerView(UpdateView):
	"""Предстовление изменения статистики игрока"""
	template_name = 'edit_stat_player.html'
	model = PlayerStat
	fields = ['player']


class DeleteStatPlayerView(DeleteView):
	"""Предстовление удаления статистики игрока"""
	model = PlayerStat
	success_url = '/stat_players/'


class AddPlayerView(CreateView):
	"""Предстовление добавления игрока"""
	template_name = 'edit_player.html'
	model = Player
	fields = ['full_name', 'team', 'photo']


class UpdatePlayerView(UpdateView):
	"""Предстовление изменения игрока"""
	template_name = 'edit_player.html'
	model = Player
	fields = ['full_name', 'team', 'photo']


class DeletePlayerView(DeleteView):
	"""Предстовление удаления игрока"""
	model = Player
	success_url = '/stat_players/'


# Прошедшие игры
class StatPastGamesView(ListView):
	"""Предстовление статистики прошедших игр"""
	template_name = 'stat_old_games.html'
	queryset = PastGameStat.objects.order_by('-past_game.date_creation')
	paginate_by = 12

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['fields'] = PastGameStat._meta.fields
		return context


class AddStatPastGameView(CreateView):
	"""Предстовление добавления статистики прошедших игр"""
	template_name = 'edit_stat_old_game.html'
	model = PastGameStat
	fields = ['past_game']


class UpdateStatPastGameView(UpdateView):
	"""Предстовление изменения статистики прошедших игр"""
	template_name = 'edit_stat_old_game.html'
	model = PastGameStat
	fields = ['past_game']


class DeleteStatPastGameView(DeleteView):
	"""Предстовление удаления статистики прошедших игр"""
	model = PastGameStat
	success_url = '/stat_old_games/'


class AddPastGameView(CreateView):
	"""Предстовление добавления прошедших игр"""
	template_name = 'edit_old_game.html'
	model = PastGame
	fields = ['team_one', 'team_two', 'date', 'result']


class UpdatePastGameView(UpdateView):
	"""Предстовление изменения прошедших игр"""
	template_name = 'edit_old_game.html'
	model = PastGame
	fields = ['team_one', 'team_two', 'date', 'result']


class DeletePastGameView(DeleteView):
	"""Предстовление удаления прошедших игр"""
	model = PastGame
	success_url = '/stat_old_games/'
