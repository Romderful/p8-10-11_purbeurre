"""Favourites views."""


from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.core.paginator import Paginator
from apps.snacks.models import Substitute


@login_required
def get_favourites(request):
    """Return the user's favourites page."""
    user_email = request.session["user_email"]
    user = User.objects.get(email=user_email)
    favs = Substitute.objects.filter(user=user)
    favourites = []
    for fav in favs:
        favourites.append(fav.product)
    paginator = Paginator(favourites, 9)
    page = request.GET.get("page")
    favourites = paginator.get_page(page)
    context = {"favourites": favourites}
    return render(request, "favourites/favourites.html", context)
