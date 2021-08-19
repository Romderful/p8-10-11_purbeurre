"""Favourites urls."""


from django.urls import path
from .views import get_favourites, delete_favourite


urlpatterns = [
    path("my_favourites/", get_favourites, name="my_favourites"),
    path("my_favourites/delete/<int:id>/", delete_favourite, name="delete_favourite"),
]
