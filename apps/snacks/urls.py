"""Snacks urls."""


from django.urls import path
from .views import search_product, detail_product, save_substitute


urlpatterns = [
    path("search/", search_product, name="search_product"),
    path("detail/<id>/", detail_product, name="detail_product"),
    path("search/save/<int:id>/", save_substitute, name="save_substitute"),
]
