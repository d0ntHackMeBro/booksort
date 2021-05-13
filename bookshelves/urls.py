from django.urls import path
from .views import AddBookView, BookListView, DeleteBookView, NameShelfView, UpdateBookView, UpdateShelfView, shelf_view

app_name = 'bookshelf'


urlpatterns = [
    path('book/<int:pk>/update/', UpdateBookView.as_view(), name="update-book"),
    path('book/<int:pk>/delete/', DeleteBookView.as_view(), name="delete-book"),
    path('name-shelf/', NameShelfView.as_view(), name="name-shelf"),
    path('edit-shelf/<int:pk>/', UpdateShelfView.as_view(), name="update-shelf"),
    path('add-book/', AddBookView.as_view(), name="add-book"),
    path('book-list/', BookListView.as_view(), name="book-list"),
    path('shelf-view/', shelf_view, name="shelf-view"),
]
