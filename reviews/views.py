from django.views.generic import ListView, DetailView, FormView, UpdateView
from django.shortcuts import redirect, reverse
from reviews.models import Review
from movies.models import Movie
from books.models import Book
from reviews.forms import CreateReviewForm

# Create your views here.

class ReviewsView(ListView):
  model = Review
  paginate_by = 15
  ordering = "created"
  paginate_orphans = 5
  context_object_name = "reviews"
  template_name = "reviews/review_list.html"


class ReviewDetail(DetailView):
  model = Review
  template_name = "reviews/review_detail.html"


class CreateReview(FormView):
  model = Review
  template_name = "reviews/review_form.html"
  form_class = CreateReviewForm

  def form_valid(self, form):
    pk = self.kwargs.get("pk")
    review_type = self.request.GET.get('type')
    if review_type == 'movie':
      movie = Movie.objects.get(pk=pk)
      review = form.save()
      review.movie = movie
      review.created_by = self.request.user
      review.save()
      return redirect(reverse("movies:movie", kwargs={"pk": pk}))
    if review_type == 'book':
      book = Book.objects.get(pk=pk)
      review = form.save()
      review.book = book
      review.created_by = self.request.user
      review.save()
      return redirect(reverse("books:book", kwargs={"pk": pk}))


class UpdateReview(UpdateView):
  model = Review
  template_name = "reviews/review_form.html"
  pk_url_kwarg = 'review_pk'
  form_class = CreateReviewForm

  def form_valid(self, form):
    self.object.save()
    return super().form_valid(form)

  def get_success_url(self):
    review_type = self.request.GET.get('type')
    pk = self.kwargs.get("item_pk")
    if review_type == 'movie':
      return reverse("movies:movie", kwargs={"pk": pk})
    if review_type == 'book':
      return reverse("books:book", kwargs={"pk": pk})


def delete_review(request, pk):
  user = request.user
  review_type = request.GET.get('type')
  try:
    if review_type == 'movie':
      review = Review.objects.get(movie=pk, created_by=user)
      print(review)
      review.delete()
      return redirect(reverse("movies:movie", kwargs={"pk": pk}))
    if review_type == 'book':
      review = Review.objects.get(book=pk, created_by=user)
      review.delete()
      return redirect(reverse("books:book", kwargs={"pk": pk}))
  except Review.DoesNotExist:
    return redirect(reverse("core:home"))