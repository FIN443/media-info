from django.urls import path
from favs.views import save_favlist
from favs.views import FavListView

app_name="favs"

urlpatterns = [
  path("", FavListView.as_view(), name="list"),
  path("add/<int:pk>/", save_favlist, name="add")
]
