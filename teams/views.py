from django.views.generic.base import TemplateView
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


class DeleteStatTeamView(DeleteView):
	"""Предстовление удаления статистики команды"""
	model = TeamStat
	success_url = '/stat_teams/'


class AddTeamView(CreateView):
	"""Предстовление добавления команды"""
	template_name = 'edit_team.html'
	model = Team
	fields = ['name', 'logo']


class UpdateTeamView(UpdateView):
	"""Предстовление изменения команды"""
	template_name = 'edit_team.html'
	model = Team
	fields = ['name', 'logo']


class DeleteTeamView(DeleteView):
	"""Предстовление удаления команды"""
	model = Team
	success_url = '/stat_teams/'


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
class StatPastGamesView(TemplateView):
	"""Предстовление статистики прошедших игр"""
	template_name = 'stat_old_games.html'


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
