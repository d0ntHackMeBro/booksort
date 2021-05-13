from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, reverse
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import AddBookForm, NameShelfForm
from .models import Book, Shelf


@login_required
def shelf_view(request):
    user = request.user
    context = {
        'user': user,
        'shelf': Shelf.objects.get(user=user),
        'books': Book.objects.filter(user=user)
    }
    return render(request, 'bookshelves/shelf_view.html', context)


class NameShelfView(LoginRequiredMixin, CreateView):
    template_name = 'bookshelves/name_shelf.html'
    form_class = NameShelfForm

    def get_success_url(self):
        return reverse("bookshelf:shelf-view")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UpdateShelfView(LoginRequiredMixin, UpdateView):
    template_name = 'bookshelves/update_shelf.html'
    queryset = Shelf.objects.all()
    form_class = NameShelfForm

    def get_success_url(self):
        return reverse("users:profile")


class AddBookView(LoginRequiredMixin, CreateView):
    template_name = 'bookshelves/add_book.html'
    form_class = AddBookForm

    def get_success_url(self):
        return reverse("bookshelf:shelf-view")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class BookListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'bookshelves/book_list.html'
    context_object_name = 'books'

    def get_queryset(self):
        user = self.request.user
        qs = super().get_queryset()
        return qs.filter(user=user)


class UpdateBookView(LoginRequiredMixin, UpdateView):
    template_name = 'bookshelves/update_book.html'
    queryset = Book.objects.all()
    form_class = AddBookForm
    context_object_name = "book"

    def get_success_url(self):
        return reverse("bookshelf:book-list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class DeleteBookView(LoginRequiredMixin, DeleteView):
    template_name = 'bookshelves/delete_book.html'
 #   queryset = Book.objects.all()

    def get_queryset(self):
        user = self.request.user
        return Book.objects.filter(user=user)

    def get_success_url(self):
        return reverse('bookshelf:book-list')
