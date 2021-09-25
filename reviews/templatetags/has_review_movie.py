from django import template
from reviews.models import Review

register = template.Library()

@register.simple_tag(takes_context=True)
def has_review_movie(context, movie):
  user = context.request.user
  review = Review.objects.filter(created_by=user, movie=movie)
  if review:
    return True
    