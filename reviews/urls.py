from django.urls import path
from reviews.views import ReviewsView, ReviewDetail, CreateReview, UpdateReview, delete_review

app_name="reviews"

urlpatterns = [
  path("", ReviewsView.as_view(), name="reviews"),
  path("<int:pk>", ReviewDetail.as_view(), name="review"),
  path("<int:review_pk>/update/<int:item_pk>", UpdateReview.as_view(), name="update"),
  path("<int:pk>/delete", delete_review, name="delete"),
  path("<int:pk>/create", CreateReview.as_view(), name="create"),
]
