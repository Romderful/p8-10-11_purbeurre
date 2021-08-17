"""Test the views."""


from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse
from apps.snacks.models import Product, Substitute


class TestViews(TestCase):
    """Test the views."""

    def setUp(self):
        """Set up config."""
        self.client = Client()
        self.session = self.client.session
        self.session["user_email"] = "test@email.com"
        self.session.save()
        self.my_favourites_url = reverse("my_favourites")

        User = get_user_model()
        self.user = User.objects.create_user(  # type: ignore
            username="testname", email=self.session["user_email"], password="Secret"
        )
        self.product = Product.objects.create(
            name="saumon",
            description="testdescription",
            store="teststore",
            url="testurl",
            grade="b",
            image="testimage",
            salt=1.0,
            carbohydrates=1.0,
            sugars=1.0,
            fats=1.0,
            proteins=1.0,
        )
        self.favourite = Substitute.objects.create(user=self.user, product=self.product)

    def test_get_favourites(self):
        """Test get_favourites view."""
        self.client.force_login(self.user)  # type: ignore
        response = self.client.get(self.my_favourites_url)
        if self.assertEquals(response.status_code, 200):
            self.assertTemplateUsed(response, "favourites/favourites.html")

    def test_favourite_in_context(self):
        """Test product is in favourites context."""
        self.client.force_login(self.user)  # type: ignore
        response = self.client.get(self.my_favourites_url)
        self.assertIn(self.product, response.context["favourites"])
