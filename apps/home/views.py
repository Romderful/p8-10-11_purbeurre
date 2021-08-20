"""Home views."""


from django.shortcuts import render


# Create your views here.
def home(request):
    """Return home html template."""
    return render(request, "pages/home.html")


def legal_notice(request):
    """Return home html template."""
    return render(request, "pages/legal_notice.html")
