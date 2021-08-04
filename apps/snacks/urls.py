"""Snacks urls."""


from django.urls import path
from .views import search_product, detail_product


urlpatterns = [
    path("search/", search_product, name="search_product"),
    path("<substitute_id>/", detail_product, name="detail_product"),
]
