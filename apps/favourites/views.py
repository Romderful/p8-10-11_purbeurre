"""Favourites views."""


from django.contrib.auth.decorators import login_required
from apps.accounts.authenticate import get_user_model
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from apps.snacks.models import Substitute, Product


@login_required
def get_favourites(request):
    """Return the user's favourites page."""
    current_user = request.user
    user = get_user_model().objects.get(id=current_user.id)
    favs = Substitute.objects.filter(user=user)
    favourites = []
    for fav in favs:
        favourites.append(fav.product)
    paginator = Paginator(favourites, 9)
    page = request.GET.get("page")
    favourites = paginator.get_page(page)
    context = {"favourites": favourites}
    return render(request, "favourites/favourites.html", context)


def delete_favourite(request, id):
    """Delete a saved substitute."""
    current_user = request.user
    user = get_user_model().objects.get(id=current_user.id)
    product = Product.objects.get(pk=id)
    Substitute.objects.filter(user=user, product=product).delete()
    return redirect(request.META.get("HTTP_REFERER", "/"))
