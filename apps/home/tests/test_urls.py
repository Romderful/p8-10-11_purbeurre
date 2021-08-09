"""Test the urls."""


from apps.home.views import home, legal_notice
from django.test import SimpleTestCase
from django.urls import reverse, resolve


class TestUrls(SimpleTestCase):
    """Test the urls."""

    def test_home_url_is_resolved(self):
        """Test if the home url is resolved."""
        url = reverse("home")
        self.assertEqual(resolve(url).func, home)

    def test_legal_notice_url_is_resolved(self):
        """Test if the legal notice url is resolved."""
        url = reverse("legal_notice")
        self.assertEqual(resolve(url).func, legal_notice)
