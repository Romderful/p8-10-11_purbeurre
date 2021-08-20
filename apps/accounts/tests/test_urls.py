"""Test the urls."""


from apps.accounts.views import profile, SignUpView
from django.test import SimpleTestCase
from django.urls import reverse, resolve


class TestUrls(SimpleTestCase):
    """Test the urls."""

    def test_profile_url_is_resolved(self):
        """Test if the profile url is resolved."""
        url = reverse("profile")
        self.assertEqual(resolve(url).func, profile)

    def test_signup_url_is_resolved(self):
        """Test if the signup url is resolved."""
        url = reverse("signup")
        self.assertEqual(resolve(url).func.__name__, SignUpView.as_view().__name__)
