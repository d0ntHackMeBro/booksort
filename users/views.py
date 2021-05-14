from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, reverse
from django.views import generic

from .forms import UserRegisterForm
from bookshelf.models import Bookshelf


def index(request):
    if request.user.is_authenticated:
        return redirect('users:profile')
    else:
        return redirect('users:register')


@login_required
def profile(request):
    user = request.user
    if len(Bookshelf.objects.filter(user=user)) > 0:
        bookshelf = Bookshelf.objects.get(user=user)
    else:
        bookshelf = None
    context = {
        'user': user,
        'bookshelf': bookshelf
    }
    return render(request, 'profile.html', context)


class RegisterView(generic.CreateView):
    template_name = 'register.html'
    form_class =  UserRegisterForm

    def get_success_url(self):
        return reverse('users:profile')
