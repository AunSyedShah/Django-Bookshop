from django import forms
from .models import Book


class AddBookForm(forms.ModelForm):
    class Meta:
        fields = ["book_name", "book_code", "quantity_available"]
