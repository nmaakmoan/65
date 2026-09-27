from django.urls import path
from .views import users, notes

urlpatterns = [
    path('users/', users),
    path('notes/', notes),
]