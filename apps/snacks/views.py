"""Snacks views."""


from django.shortcuts import render
from .models import Product


def search(request):
    """Research a product."""
    query = request.GET.get("query")
    if not query:
        products = Product.objects.all()
    else:
        products = Product.objects.filter(name__icontains=query)
    context = {"products": products}
    return render(request, "snacks/search.html", context)
