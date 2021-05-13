from django import forms
from .models import Book, Bookshelf


class BookCreateForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['isbn', 'title', 'author', 'spine_width', 'spine_height', 'image']

class BookshelfCreateForm(forms.ModelForm):
    class Meta:
        model = Bookshelf
        fields = ['name']
