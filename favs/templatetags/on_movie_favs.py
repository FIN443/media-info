from django import template
from favs.models import FavList

register = template.Library()

@register.simple_tag(takes_context=True)
def on_movie_favs(context, movie):
  user = context.request.user
  the_list, _ = FavList.objects.get_or_create(created_by=user)
  fav_movies = the_list.movies.all()
  return movie in fav_movies