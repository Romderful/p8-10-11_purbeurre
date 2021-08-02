"""Snacks views."""


from django.shortcuts import render
from .models import Product


def search_product(request):
    """Search a product."""
    product_found = Product()
    try:
        query = request.GET.get("query")
        if not query:
            raise IndexError
        product = Product.objects.filter(name__icontains=query).first()
        my_substitutes = product_found.get_substitutes(product)
        context = {"product": product, "my_substitutes": my_substitutes}
        return render(request, "snacks/search.html", context)
    except IndexError:
        return render(request, "snacks/notfound.html")
