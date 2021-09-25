from django import forms
from reviews.models import Review


class CreateReviewForm(forms.ModelForm):
  class Meta:
    model = Review
    fields = (
      "text",
      "rating",
    )

  text = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "10 ~ 100 characters."}))
  rating = forms.IntegerField()

  def clean_text(self):
    text = self.cleaned_data.get("text")
    if len(text) < 10 or len(text) > 100:
      print(len(text))
      raise forms.ValidationError("Not 10 ~ 100 characters.")
    else:
      return text

  def clean_rating(self):
    rating = self.cleaned_data.get("rating")
    if rating < 1 or rating > 5:
      raise forms.ValidationError("Rating must be 1 ~ 5.")
    else:
      return rating

  def save(self):
    review = super().save(commit=False)
    return review