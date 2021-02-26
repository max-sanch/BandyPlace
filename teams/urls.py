from django.urls import path
from teams import views

# URL teams app
urlpatterns = [
	# Статистика команд
	path('stat/teams/', views.StatTeamsView.as_view(), name='stat_teams'),
	path('stat/team/add/', views.AddStatTeamView.as_view(), name='add_stat_team'),
	path('stat/team/update/<int:pk>/', views.UpdateStatTeamView.as_view(), name='update_stat_team'),
	path('stat/team/delete/<int:pk>/', views.DeleteStatTeamView.as_view(), name='delete_stat_team'),
	# Редактирование команд
	path('add_team/', views.AddTeamView.as_view(), name='add_team'),
	path('update_team/<int:pk>/', views.UpdateTeamView.as_view(), name='update_team'),
	path('delete_team/<int:pk>/', views.DeleteTeamView.as_view(), name='delete_team'),

	# Статистика играков
	path('stat/players/', views.StatPlayersView.as_view(), name='stat_players'),
	path('stat/player/add/', views.AddStatPlayerView.as_view(), name='add_stat_player'),
	path('stat/player/update/<int:pk>/', views.UpdateStatPlayerView.as_view(), name='update_stat_player'),
	path('stat/player/delete/<int:pk>/', views.DeleteStatPlayerView.as_view(), name='delete_stat_player'),
	# Редактирование играков
	path('add_player/', views.AddPlayerView.as_view(), name='add_player'),
	path('update_player/<int:pk>/', views.UpdatePlayerView.as_view(), name='update_player'),
	path('delete_player/<int:pk>/', views.DeletePlayerView.as_view(), name='delete_player'),

	# Статистика игр
	path('stat/old_games/', views.StatPastGamesView.as_view(), name='stat_old_games'),
	path('stat/old_game/add/', views.AddStatPastGameView.as_view(), name='add_stat_old_game'),
	path('stat/old_game/update/<int:pk>/', views.UpdateStatPastGameView.as_view(), name='update_stat_old_game'),
	path('stat/old_game/delete/<int:pk>/', views.DeleteStatPastGameView.as_view(), name='delete_stat_old_game'),
	# Редактирование игр
	path('add_old_game/', views.AddPastGameView.as_view(), name='add_old_game'),
	path('update_old_game/<int:pk>/', views.UpdatePastGameView.as_view(), name='update_old_game'),
	path('delete_old_game/<int:pk>/', views.DeletePastGameView.as_view(), name='update_old_game'),
]
