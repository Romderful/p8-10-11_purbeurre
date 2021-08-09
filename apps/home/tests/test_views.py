"""Test the views."""


from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):
    """Test the views."""

    def test_home_get(self):
        """Test home view."""
        client = Client()
        response = client.get(reverse("home"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "home/home.html")

    def test_legal_notice_get(self):
        """Test legal_notice view."""
        client = Client()
        response = client.get(reverse("legal_notice"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "home/legal_notice.html")
