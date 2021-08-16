"""Test the views."""


from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):
    """Test the views."""

    def setUp(self):
        """Set up config."""
        self.client = Client()
        self.session = self.client.session
        self.session["user_email"] = "test@email.com"
        self.session.save()
        self.my_favourites_url = reverse("my_favourites")

    def test_get_favourites(self):
        """Test get_favourites view."""
        self.client.force_login(
            get_user_model().objects.get_or_create(email=self.session["user_email"])[0]
        )
        response = self.client.get(self.my_favourites_url)
        if self.assertEquals(response.status_code, 200):
            self.assertTemplateUsed(response, "favourites/favourites.html")
