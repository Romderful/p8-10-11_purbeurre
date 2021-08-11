"""Snacks models."""


from config import settings
from django.db import models


class Category(models.Model):
    """Category table."""

    name = models.CharField(max_length=100, unique=True)


class Product(models.Model):
    """Product table."""

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    store = models.CharField(max_length=50)
    url = models.URLField(max_length=255)
    grade = models.CharField(max_length=1)
    image = models.CharField(max_length=255)
    salt = models.FloatField(null=True)
    carbohydrates = models.FloatField(null=True)
    sugars = models.FloatField(null=True)
    fats = models.FloatField(null=True)
    proteins = models.FloatField(null=True)
    categories = models.ManyToManyField(Category)

    def get_substitutes(self, product):
        """Return the substitutes queryset."""
        cleaned_substitutes = []
        substitute_categories = []
        product_categories = product.categories.all()
        for category in product_categories:
            substitute_categories.append(category.id)
        my_substitutes = Product.objects.filter(categories__in=substitute_categories)
        for substitute in my_substitutes:
            if substitute not in cleaned_substitutes and substitute != product:
                if ord(substitute.grade) <= ord(product.grade):
                    cleaned_substitutes.append(substitute)
        return cleaned_substitutes


class Substitute(models.Model):
    """Substitute table."""

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
