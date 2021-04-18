from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import PermissionRequiredMixin


class HomePageView(TemplateView):
	"""Представление главное страницы"""
	template_name = 'index.html'


class AccountView(PermissionRequiredMixin, TemplateView):
	"""Представление аккаунта пользователя"""
	template_name = 'account.html'
	permission_required = ('user.is_staff', )
