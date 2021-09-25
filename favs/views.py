from django.views.generic import ListView
from django.shortcuts import render, redirect, reverse
from favs.models import FavList
from movies.models import Movie
from books.models import Book

# Create your views here.
class FavListView(ListView):
  model = FavList
  ordering = "-created_at"
  context_object_name = "favs"
  template_name = "favs/fav_list.html"


def save_favlist(request, pk):
  fav_type = request.GET.get("type", None)
  action = request.GET.get("action", None)
  if fav_type == "movie":
    movie = Movie.objects.get(pk=pk)
    the_list, _ = FavList.objects.get_or_create(created_by=request.user)
    if action == "add":
      the_list.movies.add(movie)
    elif action == "remove":
      the_list.movies.remove(movie)
    return redirect(reverse("movies:movie", kwargs={'pk': pk}))

  if fav_type == "book":
    book = Book.objects.get(pk=pk)
    the_list, _ = FavList.objects.get_or_create(created_by=request.user)
    if action == "add":
      the_list.books.add(book)
    elif action == "remove":
      the_list.books.remove(book)
    return redirect(reverse("books:book", kwargs={'pk': pk}))
    
  return redirect(reverse("core:home"))