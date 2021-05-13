from django.urls import path
from .views import (
    BookCreateView,
    BookListView,
    BookDeleteView,
    BookshelfCreateView,
    BookUpdateView,
    BookshelfUpdateView,
    bookshelf_view
)

app_name = 'bookshelf'


urlpatterns = [
    path('', bookshelf_view, name="bookshelf-view"),
    path('book/<int:pk>/update/', BookUpdateView.as_view(), name="book-update"),
    path('book/<int:pk>/delete/', BookDeleteView.as_view(), name="book-delete"),
    path('name-bookshelf/', BookshelfCreateView.as_view(), name="bookshelf-create"),
    path('rename-bookshelf/<int:pk>/', BookshelfUpdateView.as_view(), name="bookshelf-update"),
    path('add-book/', BookCreateView.as_view(), name="book-create"),
    path('book-list/', BookListView.as_view(), name="book-list"),
]
