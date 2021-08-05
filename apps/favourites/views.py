"""Favourites views."""


from django.shortcuts import render, redirect


def get_favourites(request):
    """Test."""
    if not request.user.is_authenticated:
        return redirect("/users/sign_in")
    return render(request, "favourites/favourites.html")
