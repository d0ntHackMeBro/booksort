from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, reverse
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import BookCreateForm, BookshelfCreateForm
from .models import Book, Bookshelf


@login_required
def bookshelf_view(request):
    user = request.user
    context = {
        'user': user,
        'bookshelf': Bookshelf.objects.get(user=user),
        'books': Book.objects.filter(user=user)
    }
    return render(request, 'bookshelf_view.html', context)


class BookshelfCreateView(LoginRequiredMixin, CreateView):
    template_name = 'bookshelf_create.html'
    form_class = BookshelfCreateForm

    def get_success_url(self):
        return reverse("bookshelf:bookshelf-view")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class BookshelfUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'bookshelf_update.html'
    queryset = Bookshelf.objects.all()
    form_class = BookshelfCreateForm

    def get_success_url(self):
        return reverse("users:profile")


class BookCreateView(LoginRequiredMixin, CreateView):
    template_name = 'book_create.html'
    form_class = BookCreateForm

    def get_success_url(self):
        return reverse("bookshelf:bookshelf-view")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class BookListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'

    def get_queryset(self):
        user = self.request.user
        qs = super().get_queryset()
        return qs.filter(user=user)


class BookUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'book_update.html'
    queryset = Book.objects.all()
    form_class = BookCreateForm
    context_object_name = "book"

    def get_success_url(self):
        return reverse("bookshelf:book-list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class BookDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'book_delete.html'

    def get_queryset(self):
        user = self.request.user
        return Book.objects.filter(user=user)

    def get_success_url(self):
        return reverse('bookshelf:book-list')
