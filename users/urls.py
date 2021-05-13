from django.urls import path

from .views import index, profile, RegisterView

app_name = 'users'


urlpatterns = [
    path('', index, name="index"),
    path('profile/', profile, name='profile'),
    path('register/', RegisterView.as_view(), name='register'),
]
