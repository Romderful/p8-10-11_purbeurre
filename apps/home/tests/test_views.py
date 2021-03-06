"""Test the views."""


from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):
    """Test the views."""

    def test_home(self):
        """Test home view."""
        client = Client()
        response = client.get(reverse("home"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/home.html")

    def test_legal_notice(self):
        """Test legal_notice view."""
        client = Client()
        response = client.get(reverse("legal_notice"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/legal_notice.html")
