"""Test the views."""


from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):
    """Test the views."""

    def test_sign_up_GET(self):
        """Test sign_up view."""
        client = Client()
        response = client.get(reverse("sign_up"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "users/signup.html")
