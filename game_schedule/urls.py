from django.urls import path
from game_schedule import views

# URL game_schedule app
urlpatterns = [
	path('add/', views.AddUpcomingGameView.as_view(), name='add_new_game'),
	path('update/<int:pk>/', views.UpdateUpcomingGameView.as_view(), name='update_new_game'),
	path('delete/<int:pk>/', views.DeleteUpcomingGameView.as_view(), name='delete_new_game'),
	path('', views.UpcomingGameView.as_view(), name='all_new_games'),
]
