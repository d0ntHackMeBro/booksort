from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render, reverse
from django.views import generic

from .forms import UserRegisterForm
from .models import Profile
from bookshelves.models import Shelf


def welcome(request):
    if request.user.is_authenticated:
        return redirect('users:profile')
    else:
        return render(request, 'users/welcome.html')


class RegisterView(generic.CreateView):
    template_name = 'users/register.html'
    form_class =  UserRegisterForm

    def get_success_url(self):
        return reverse('users:profile')


@login_required
def profile(request):
    user = request.user
    if len(Shelf.objects.filter(user=user))>0:
        shelf = Shelf.objects.get(user=user)
    else:
        shelf = None
    context = {
        'user': user,
        'shelf': shelf
    }
    return render(request, 'users/profile.html', context)
