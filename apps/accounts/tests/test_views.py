"""Test the views."""


from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):
    """Test the views."""

    def setUp(self):
        """Set up config."""
        self.client = Client()
        self.signup_url = reverse("signup")
        self.login_url = reverse("login")
        self.profile_url = reverse("profile")
        self.home_url = reverse("home")

    def test_signup(self):
        """Test signup view."""
        first_response = self.client.get(self.signup_url)
        second_response = self.client.get(self.home_url)
        if self.assertEquals(first_response.status_code, 200):
            self.assertTemplateUsed(first_response, "registration/signup.html")
        elif self.assertEquals(second_response.status_code, 200):
            self.assertTemplateUsed(second_response, "home/home.html")

    def test_login(self):
        """Test login view."""
        first_response = self.client.get(self.login_url)
        second_response = self.client.get(self.home_url)
        if self.assertEquals(first_response.status_code, 200):
            self.assertTemplateUsed(first_response, "registration/login.html")
        elif self.assertEquals(second_response.status_code, 200):
            self.assertTemplateUsed(second_response, "pages/home.html")

    def test_profile(self):
        """Test profile view."""
        first_response = self.client.get(self.login_url)
        second_response = self.client.get(self.profile_url)
        if self.assertEquals(first_response.status_code, 200):
            self.assertTemplateUsed(first_response, "registration/signin.html")
        elif self.assertEquals(second_response.status_code, 302):
            self.assertTemplateUsed(second_response, "registration/profile.html")

    def test_sign_out(self):
        """Test sign_out view."""
        response = self.client.get(self.home_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/home.html")
