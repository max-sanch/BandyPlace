from django.urls import path
from videos import views

# URL videos app
urlpatterns = [
	path('all/', views.AllVideosView.as_view(), name='all_videos'),
	path('one/<slug:slug>/', views.OneVideoView.as_view(), name='one_video'),
	path('add/', views.AddVideoView.as_view(), name='add_video'),
	path('update/<slug:slug>/', views.UpdateVideoView.as_view(), name='update_video'),
	path('delete/<slug:slug>/', views.DeleteVideoView.as_view(), name='delete_video'),
]
