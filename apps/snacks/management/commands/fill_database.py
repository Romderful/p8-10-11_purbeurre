"""Custom command module."""


import requests
from django.core.management.base import BaseCommand
from apps.snacks.models import Category, Product


NAME = "product_name"
DESCRIPTION = "generic_name"
STORE = "stores"
URL = "url"
GRADE = "nutrition_grades"
IMAGE = "image_url"
CATEGORIES = "categories"
NUTRIMENTS = "nutriments"


class Command(BaseCommand):
    """Custom command."""

    def __init__(self):
        """Initialise."""
        super().__init__()
        self.product_number = 5000
        self.max_products = 0
        self.valid_products = []

    def handle(self, *args, **options):
        """Call main function of fill_database module."""
        self.stdout.write("Filling the database...")
        try:
            self.run()
            self.stdout.write("Database Filled.")
        except TypeError:
            self.stdout.write("A problem occured during the process.")

    def get_data(self, page: int) -> dict:
        """Get the data from openfoodfacts by requesting the API."""
        response = requests.get(
            "https://fr.openfoodfacts.org/cgi/search.pl",
            {
                "action": "process",
                "tagtype_0": "categories",
                "tagtype_1": "countries",
                "tag_contains_1": "france",
                "page_size": 50,
                "page": page,
                "json": 1,
            },
        )
        response.raise_for_status()
        data = response.json()
        return data

    def get_valid_products(self, data: dict):
        """Append a dict containing all the product ressources required to a list.

        Filter the data by len.
        """
        for index, product in enumerate(data["products"]):
            try:
                new_product = {
                    NAME: product[NAME],
                    DESCRIPTION: product[DESCRIPTION],
                    STORE: product[STORE],
                    URL: product[URL],
                    GRADE: product[GRADE],
                    IMAGE: product[IMAGE],
                    CATEGORIES: product[CATEGORIES],
                    NUTRIMENTS: product[NUTRIMENTS],
                }
            except KeyError:
                pass
            else:
                if (
                    len(product[NAME]) in range(1, 51)
                    and len(product[DESCRIPTION]) in range(1, 256)
                    and len(product[STORE]) in range(1, 51)
                    and len(product[URL]) in range(1, 256)
                    and len(product[IMAGE]) in range(1, 256)
                    and len(product[CATEGORIES]) in range(1, 101)
                ):
                    self.valid_products.append(new_product)

    def run(self):
        """Launch the script from this function."""
        user_choice = self.product_number
        self.max_products = user_choice
        page = 1
        while len(self.valid_products) <= self.max_products:
            data = self.get_data(page)
            self.get_valid_products(data)
            page += 1
        self.valid_products = self.valid_products[: self.max_products]

        for product in self.valid_products:

            fats = None
            proteins = None
            carbohydrates = None
            sugars = None
            salt = None

            if "fat_100g" in product[NUTRIMENTS]:
                fats = product[NUTRIMENTS]["fat_100g"]
            if "proteins_100g" in product[NUTRIMENTS]:
                proteins = product[NUTRIMENTS]["proteins_100g"]
            if "carbohydrates_100g" in product[NUTRIMENTS]:
                carbohydrates = product[NUTRIMENTS]["carbohydrates_100g"]
            if "sugars_100g" in product[NUTRIMENTS]:
                sugars = product[NUTRIMENTS]["sugars_100g"]
            if "salt_100g" in product[NUTRIMENTS]:
                salt = product[NUTRIMENTS]["salt_100g"]

            created_product, created = Product.objects.update_or_create(
                name=product[NAME],
                description=product[DESCRIPTION],
                store=product[STORE],
                url=product[URL],
                grade=product[GRADE],
                image=product[IMAGE],
                fats=fats,
                proteins=proteins,
                carbohydrates=carbohydrates,
                sugars=sugars,
                salt=salt,
            )

            categories = [
                category.strip().lower() for category in product[CATEGORIES].split(",")
            ]

            for category in categories:
                created_category, created = Category.objects.update_or_create(
                    name=category
                )
                created_product.categories.add(created_category)
