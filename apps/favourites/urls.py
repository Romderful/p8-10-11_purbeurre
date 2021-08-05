from django.urls import path
from .views import get_favourites


urlpatterns = [
    path("my_favourites/", get_favourites, name="my_favourites"),
]
