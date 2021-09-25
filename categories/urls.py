from django.urls import path
from categories.views import resolve_categories

app_name="categories"

urlpatterns = [
  path("", resolve_categories, name="categories")
]
