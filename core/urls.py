from django.urls import path
from core.views import resolve_home, resolve_search, CategoryDetail

app_name="core"

urlpatterns = [
  path("", resolve_home, name="home"),
  path("search/", resolve_search, name="search"),
  path("search/<int:pk>/", CategoryDetail.as_view(), name="category")
]
