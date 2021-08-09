"""Test the urls."""


from apps.favourites.views import get_favourites
from django.test import SimpleTestCase
from django.urls import reverse, resolve


class TestUrls(SimpleTestCase):
    """Test the urls."""

    def test_my_favourites_url_is_resolved(self):
        """Test if the my_favourites url is resolved."""
        url = reverse("my_favourites")
        self.assertEqual(resolve(url).func, get_favourites)
