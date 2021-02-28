from django.contrib.auth import views as auth_views
from django.urls import path

from core import views

# URL core app
urlpatterns = [
	path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
	path('account/', views.AccountView.as_view(), name='account'),
	path('', views.HomePageView.as_view(), name='home'),
]
