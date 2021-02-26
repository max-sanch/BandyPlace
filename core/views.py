from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
	"""Представление главное страницы"""
	template_name = 'index.html'


class AccountView(TemplateView):
	"""Представление аккаунта пользователя"""
	template_name = 'account.html'
