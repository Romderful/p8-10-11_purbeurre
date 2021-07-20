"""Test the urls."""


from apps.users.views import profile, sign_in, sign_out, sign_up
from django.test import SimpleTestCase
from django.urls import reverse, resolve


class TestUrls(SimpleTestCase):
    """Test the urls."""

    def test_profile_url_is_resolved(self):
        """Test if the profile url is resolved."""
        url = reverse("profile")
        self.assertEqual(resolve(url).func, profile)

    def test_sign_in_url_is_resolved(self):
        """Test if the sign_in url is resolved."""
        url = reverse("sign_in")
        self.assertEqual(resolve(url).func, sign_in)

    def test_sign_out_url_is_resolved(self):
        """Test if the sign_out url is resolved."""
        url = reverse("sign_out")
        self.assertEqual(resolve(url).func, sign_out)

    def test_sign_up_url_is_resolved(self):
        """Test if the sign_up url is resolved."""
        url = reverse("sign_up")
        self.assertEqual(resolve(url).func, sign_up)
