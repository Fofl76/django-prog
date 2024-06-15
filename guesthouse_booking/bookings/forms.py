from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['room', 'rating', 'comment', 'review_date']  # Добавьте 'review_date'
