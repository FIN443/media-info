from django.shortcuts import render
from django.views.generic import DetailView
from movies.models import Movie
from books.models import Book
from people.models import Person
from categories.models import Category

def resolve_home(request):
  

  movies = Movie.objects.all().order_by('-pk')[:10]
  books = Book.objects.all().order_by('-pk')[:10]
  people = Person.objects.all().order_by('-pk')[:10]
  

  return render(request, "home.html", {
    "movies":movies,
    "books": books,
    "people": people,
    "page_title": "Home"
  })



def resolve_search(request):
  name = request.GET.get("name","Anything")
  name = str.capitalize(name)
  people = Person.objects.filter(name__contains=name)
  movies = Movie.objects.filter(title__contains=name)
  books = Book.objects.filter(title__contains=name)

  return render(request, "search.html", {
    "categories": Category.objects.all(),
    "name":name,
    "people":people,
    "movies":movies,
    "books":books,
  })


  
class CategoryDetail(DetailView):
  model = Category
  context_object_name = 'category'
  template_name = "categories/category_detail.html"	