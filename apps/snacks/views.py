"""Snacks views."""


from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Product, Substitute
from apps.accounts.authenticate import get_user_model


def search_product(request):
    """Return the search page.

    Contains the requested product with its substitutes.
    """
    try:
        query = request.GET.get("query")
        if not query:
            raise IndexError
        product_found = Product.objects.filter(name__icontains=query).first()
        try:
            substitutes_list = product_found.get_substitutes()  # type: ignore
            paginator = Paginator(substitutes_list, 6)
            page = request.GET.get("page")
            substitutes = paginator.get_page(page)
        except AttributeError:
            return render(request, "snacks/notfound.html")
        context = {"product": product_found, "substitutes": substitutes, "query": query}
        return render(request, "snacks/search.html", context)
    except IndexError:
        return render(request, "snacks/notfound.html")


def detail_product(request, id):
    """Return the selected product detail page."""
    product = Product.objects.get(pk=id)
    context = {"product": product}
    return render(request, "snacks/detail.html", context)


def save_substitute(request, id):
    """Save the wanted substitute."""
    current_user = request.user
    user = get_user_model().objects.get(id=current_user.id)
    product = Product.objects.get(pk=id)
    if not Substitute.objects.filter(user=user, product=product).exists():
        messages.success(request, "Article enregistré !")
        Substitute.objects.create(user=user, product=product)
    else:
        messages.error(request, "Article déjà possédé ! ")
    return redirect(request.META.get("HTTP_REFERER", "/"))
