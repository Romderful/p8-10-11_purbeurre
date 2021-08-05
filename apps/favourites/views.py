from django.shortcuts import render


def get_favourites(request):
    """Test."""
    return render(request, "favourites/favourites.html")
