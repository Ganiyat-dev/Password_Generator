from django.urls import path
from .views import HomeView, PasswordView
urlpatterns = [
    path('', HomeView, name='home'),
    path('password_generator/', PasswordView, name='password'),
]