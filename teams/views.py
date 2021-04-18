from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Team, TeamStat, Player, PlayerStat, PastGame


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
	template_name = 'old_games.html'
	queryset = PastGame.objects.order_by('date', 'time')
	paginate_by = 12


class AddPastGameView(CreateView):
	"""Предстовление добавления прошедших игр"""
	template_name = 'edit_old_game.html'
	model = PastGame
	fields = ['team_one', 'team_two', 'result', 'date', 'time', 'address']
	success_url = reverse_lazy('add_old_game')


class UpdatePastGameView(UpdateView):
	"""Предстовление изменения прошедших игр"""
	template_name = 'edit_old_game.html'
	model = PastGame
	fields = ['team_one', 'team_two', 'result', 'date', 'time', 'address']
	success_url = reverse_lazy('old_games')


class DeletePastGameView(DeleteView):
	"""Предстовление удаления прошедших игр"""
	template_name = 'delete_old_game.html'
	model = PastGame
	success_url = reverse_lazy('old_games')
