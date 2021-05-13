from django import forms
from .models import Book, Shelf


class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['isbn', 'title', 'author', 'spine_width', 'spine_height', 'image']

class NameShelfForm(forms.ModelForm):
    class Meta:
        model = Shelf
        fields = ['name']
