"""Test the models."""


from django.contrib.auth import get_user_model
from apps.snacks.models import Category, Product, Substitute
from django.test import TestCase


class ProductTests(TestCase):
    """Test the models."""

    def setUp(self):
        """Set up config."""
        self.product = Product.objects.create(
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

        self.category = Category.objects.create(
            id=1,
            name="testcategory",
        )

        cat_snacks = Category.objects.get(name="testcategory")
        self.product.categories.add(cat_snacks)

    def test_product_content(self):
        """Test the database entries."""
        self.assertEqual(f"{self.product.name}", "testname")
        self.assertEqual(f"{self.product.description}", "testdescription")
        self.assertEqual(f"{self.product.store}", "teststore")
        self.assertEqual(f"{self.product.url}", "testurl")
        self.assertEqual(f"{self.product.grade}", "a")
        self.assertEqual(f"{self.product.image}", "testimage")
        self.assertEqual(f"{self.product.salt}", "1.0")
        self.assertEqual(f"{self.product.carbohydrates}", "1.0")
        self.assertEqual(f"{self.product.sugars}", "1.0")
        self.assertEqual(f"{self.product.fats}", "1.0")
        self.assertEqual(f"{self.product.proteins}", "1.0")

    def test_get_substitute(self):
        """Test get_substitute."""
        my_product = Product()
        result = my_product.get_substitutes(self.product)
        self.assertNotIn(self.product, result)


class CategoryTests(TestCase):
    """Test the models."""

    def setUp(self):
        """Set up config."""
        self.category = Category.objects.create(
            name="testname",
        )

    def test_category_content(self):
        """Test the database entries."""
        self.assertEqual(f"{self.category.name}", "testname")


class SubstituteTests(TestCase):
    """Test the models."""

    def setUp(self):
        """Set up config."""
        self.product = Product.objects.create(
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
        self.user = get_user_model().objects.create(
            username="testuser", email="test@email.com", password="secret"
        )
        self.substitute = Substitute.objects.create(
            user=self.user, product=self.product
        )

    def test_substitute_content(self):
        """Test the database entries."""
        self.assertEqual(f"{self.substitute.user}", f"{self.user}")
        self.assertEqual(f"{self.substitute.product}", f"{self.product}")
