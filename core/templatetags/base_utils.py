from django import template

from game_schedule.models import UpcomingGame
from teams.models import PastGame
from news.models import Post
from shop.models import Product

register = template.Library()


@register.simple_tag
def get_news(count):
    return Post.objects.all().order_by('date_creation')[:int(count)+1]


@register.simple_tag
def get_prods(count):
    return Product.objects.all().order_by('date_creation')[:int(count)+1]


@register.simple_tag
def get_new_games(count):
    return UpcomingGame.objects.all().order_by('date', 'time')[:int(count)+1]


@register.simple_tag
def get_old_games(count):
    return PastGame.objects.all().order_by('date', 'time')[:int(count)+1]
