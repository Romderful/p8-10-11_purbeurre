"""Test the models."""


from django.contrib.auth import get_user_model
from apps.snacks.models import Category, Product, Substitute
from django.test import TestCase


class ProductTests(TestCase):
    """Test the models."""

    def setUp(self):
        """Set up config."""
        self.chocobon = Product.objects.create(
            name="chocobon",
            description="testdescription",
            store="teststore",
            url="testurl",
            grade="c",
            image="testimage",
            salt=1.0,
            carbohydrates=1.0,
            sugars=1.0,
            fats=1.0,
            proteins=1.0,
        )

        self.chocobio = Product.objects.create(
            name="chocobio",
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

        self.saumon = Product.objects.create(
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

        self.mars = Product.objects.create(
            name="mars",
            description="testdescription",
            store="teststore",
            url="testurl",
            grade="d",
            image="testimage",
            salt=1.0,
            carbohydrates=1.0,
            sugars=1.0,
            fats=1.0,
            proteins=1.0,
        )

        self.chocolats = Category.objects.create(
            name="chocolats",
        )

        self.barrechocos = Category.objects.create(
            name="barres chocolatés",
        )

        self.fish = Category.objects.create(
            name="poisson",
        )

        self.chocobon.categories.add(self.chocolats, self.barrechocos)
        self.chocobio.categories.add(self.chocolats)
        self.saumon.categories.add(self.fish)

    def test_product_content(self):
        """Test the database entries."""
        self.assertEqual(f"{self.chocobon.name}", "chocobon")
        self.assertEqual(f"{self.chocobon.description}", "testdescription")
        self.assertEqual(f"{self.chocobon.store}", "teststore")
        self.assertEqual(f"{self.chocobon.url}", "testurl")
        self.assertEqual(f"{self.chocobon.grade}", "c")
        self.assertEqual(f"{self.chocobon.image}", "testimage")

    def test_substitute_for_better_quality(self):
        """Test potential substitutes with higher quality are returned."""
        substitutes = self.chocobon.get_substitutes()
        self.assertIn(self.chocobio, substitutes)

    def test_substitute_for_lower_quality(self):
        """Test potential substitutes with lower quality are not returned."""
        substitutes = self.chocobon.get_substitutes()
        self.assertNotIn(self.mars, substitutes)

    def test_substitute_that_have_no_linked_categories(self):
        """Test substitutes with no linked categories are not returned."""
        substitutes = self.chocobon.get_substitutes()
        self.assertNotIn(self.saumon, substitutes)


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
