from django.urls import path
from news import views

# URL news app
urlpatterns = [
	path('all/', views.AllPostsView.as_view(), name='all_posts'),
	path('one/<slug:slug>/', views.OnePostView.as_view(), name='one_post'),
	path('add/', views.AddPostView.as_view(), name='add_post'),
	path('update/<slug:slug>/', views.UpdatePostView.as_view(), name='update_post'),
	path('delete/<slug:slug>/', views.DeletePostView.as_view(), name='delete_post'),
]
