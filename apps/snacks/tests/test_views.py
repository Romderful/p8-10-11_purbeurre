"""Test the views."""


from apps.snacks.models import Product
from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):
    """Test the views."""

    def setUp(self):
        """Set up config."""
        self.client = Client()
        Product.objects.create()
        self.search_product_url = reverse("search_product")
        self.detail_product_url = reverse("detail_product", args="1")

    def test_search_product_get(self):
        """Test search_product view."""
        response = self.client.get(self.search_product_url)
        if self.assertEquals(response.status_code, 200):
            self.assertTemplateUsed(response, "snacks/notfound.html")
        elif self.assertEquals(response.status_code, 200):
            self.assertTemplateUsed(response, "snacks/search.html")

    def test_detail_product_get(self):
        """Test detail_product view."""
        response = self.client.get(self.detail_product_url)
        if self.assertEquals(response.status_code, 200):
            self.assertTemplateUsed(response, "snacks/detail.html")
