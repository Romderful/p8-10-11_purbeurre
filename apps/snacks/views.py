"""Snacks views."""


from django.shortcuts import render
from .models import Product


def search_product(request):
    """Return the search page which contains the requested product with its substitutes."""
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


def detail_product(request, substitute_id):
    """Return the selected product detail page."""
    product = Product.objects.get(pk=substitute_id)
    context = {"product": product}
    return render(request, "snacks/detail.html", context)
