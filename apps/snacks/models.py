"""Snacks models."""


from django.db import models


class Category(models.Model):
    """Category table."""

    name = models.CharField(max_length=100)


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
