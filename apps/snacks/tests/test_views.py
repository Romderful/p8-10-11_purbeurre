"""Test the views."""


from django.contrib.auth import get_user_model
from django.contrib.messages import get_messages
from apps.snacks.models import Product
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
        Product.objects.create(
            id=1,
            name="testname",
            description="testdescription",
            store="teststore",
            url="testurl",
            grade="a",
            image="testimage",
            salt=1.0,
            carbohydrates=1.0,
            sugars=1.0,
            fats=1.0,
            proteins=1.0,
        )
        self.search_product_url = reverse("search_product")
        self.detail_product_url = reverse("detail_product", args="1")
        self.save_substitute_url = reverse("save_substitute", args="1")

    def test_search_product(self):
        """Test search_product view."""
        response = self.client.get(self.search_product_url)
        if self.assertEquals(response.status_code, 200):
            self.assertTemplateUsed(response, "snacks/notfound.html")
        elif self.assertEquals(response.status_code, 200):
            self.assertTemplateUsed(response, "snacks/search.html")

    def test_detail_product(self):
        """Test detail_product view."""
        response = self.client.get(self.detail_product_url)
        if self.assertEquals(response.status_code, 200):
            self.assertTemplateUsed(response, "snacks/detail.html")

    def test_save_subtitute(self):
        """Test save_substitute view."""
        self.client.force_login(
            get_user_model().objects.get_or_create(email=self.session["user_email"])[0]
        )
        response = self.client.post(self.save_substitute_url)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "Article enregistré !")
