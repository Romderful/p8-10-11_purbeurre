"""Test the views."""


from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):
    """Test the views."""

    def setUp(self):
        """Set up config."""
        self.client = Client()
        self.sign_up_url = reverse("sign_up")
        self.sign_in_url = reverse("sign_in")
        self.profile_url = reverse("profile")
        self.home_url = reverse("home")

    def test_sign_up_GET(self):
        """Test sign_up view."""
        first_response = self.client.get(self.sign_up_url)
        second_response = self.client.get(self.home_url)
        if self.assertEquals(first_response.status_code, 200):
            self.assertTemplateUsed(first_response, "users/signup.html")
        elif self.assertEquals(second_response.status_code, 200):
            self.assertTemplateUsed(second_response, "home/home.html")

    def test_sign_in_GET(self):
        """Test sign_in view."""
        first_response = self.client.get(self.sign_in_url)
        second_response = self.client.get(self.home_url)
        if self.assertEquals(first_response.status_code, 200):
            self.assertTemplateUsed(first_response, "users/signin.html")
        elif self.assertEquals(second_response.status_code, 200):
            self.assertTemplateUsed(second_response, "home/home.html")

    def test_profile_GET(self):
        """Test profile view."""
        first_response = self.client.get(self.sign_in_url)
        second_response = self.client.get(self.profile_url)
        if self.assertEquals(first_response.status_code, 200):
            self.assertTemplateUsed(first_response, "users/signin.html")
        elif self.assertEquals(second_response.status_code, 302):
            self.assertTemplateUsed(second_response, "users/profile.html")

    def test_sign_out_GET(self):
        """Test sign_out view."""
        response = self.client.get(self.home_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "home/home.html")
