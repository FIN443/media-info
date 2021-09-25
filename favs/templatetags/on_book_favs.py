from django import template
from favs.models import FavList

register = template.Library()

@register.simple_tag(takes_context=True)
def on_book_favs(context, book):
  user = context.request.user
  the_list, _ = FavList.objects.get_or_create(created_by=user)
  fav_books = the_list.books.all()
  return book in fav_books