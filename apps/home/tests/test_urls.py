"""Test the urls."""


from apps.home.views import home
from django.test import SimpleTestCase
from django.urls import reverse, resolve


class TestUrls(SimpleTestCase):
    """Test the urls."""

    def test_home_url_is_resolved(self):
        """Test if the home url is resolved."""
        url = reverse("home")
        self.assertEqual(resolve(url).func, home)
