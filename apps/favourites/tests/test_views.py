"""Test the views."""


from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):
    """Test the views."""

    def setUp(self):
        """Set up config."""
        self.client = Client()
        self.sign_in_url = reverse("sign_in")
        self.my_favourites_url = reverse("my_favourites")

    def test_get_favourites_get(self):
        """Test get_favourites view."""
        first_response = self.client.get(self.my_favourites_url)
        second_response = self.client.get(self.sign_in_url)
        if self.assertEquals(first_response.status_code, 302):
            self.assertTemplateUsed(first_response, "favourites/favourites.html")
        elif self.assertEquals(second_response.status_code, 200):
            self.assertTemplateUsed(second_response, "users/sign_in.html")
