"""Snacks urls."""

from django.urls import path

from .views import search_product


urlpatterns = [
    path("search/", search_product, name="search_product"),
]
