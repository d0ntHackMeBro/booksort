from django.urls import path

from .views import profile, RegisterView, welcome

app_name = 'users'


urlpatterns = [
    path('', welcome, name="welcome"),
    path('profile/', profile, name='profile'),
    path('register/', RegisterView.as_view(), name='register'),
]
