"""Snacks views."""


from django.shortcuts import render
from .models import Product


def search_product(request):
    """Search a product."""
    try:
        query = request.GET.get("query")
        if not query:
            return render(request, "snacks/notfound.html")
        products = Product.objects.filter(name__icontains=query)
        product = products[0]
        context = {"product": product}
        return render(request, "snacks/search.html", context)
    except IndexError:
        return render(request, "snacks/notfound.html")
