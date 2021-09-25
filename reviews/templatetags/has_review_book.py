from django import template
from reviews.models import Review

register = template.Library()

@register.simple_tag(takes_context=True)
def has_review_book(context, book):
  user = context.request.user
  review = Review.objects.filter(created_by=user, book=book)
  if review:
    return True