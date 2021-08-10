"""Snacks views."""


from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Product, Substitute
from apps.users.models import User


def search_product(request):
    """Return the search page which contains the requested product with its substitutes."""
    product_found = Product()
    try:
        query = request.GET.get("query")
        if not query:
            raise IndexError
        product = Product.objects.filter(name__icontains=query).first()
        try:
            substitutes_list = product_found.get_substitutes(product)
            paginator = Paginator(substitutes_list, 6)
            page = request.GET.get("page")
            substitutes = paginator.get_page(page)
        except AttributeError:
            return render(request, "snacks/notfound.html")
        context = {"product": product, "substitutes": substitutes, "query": query}
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
    user_email = request.session["user_email"]
    user = User.objects.get(email=user_email)
    product = Product.objects.get(pk=id)
    if not Substitute.objects.filter(user=user, product=product).exists():
        messages.success(request, "Article enregistré !")
        Substitute.objects.create(user=user, product=product)
    else:
        messages.error(request, "Article déjà possédé ! ")
    return redirect(request.META["HTTP_REFERER"])
