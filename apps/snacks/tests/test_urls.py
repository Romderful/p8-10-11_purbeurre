"""Test the urls."""


from apps.snacks.views import search_product, detail_product
from django.test import SimpleTestCase
from django.urls import reverse, resolve


class TestUrls(SimpleTestCase):
    """Test the urls."""

    def test_search_product_url_is_resolved(self):
        """Test if the search_product url is resolved."""
        url = reverse("search_product")
        self.assertEqual(resolve(url).func, search_product)

    def test_detail_product_url_is_resolved(self):
        """Test if the detail_product url is resolved."""
        url = reverse("detail_product", args="1")
        self.assertEqual(resolve(url).func, detail_product)
