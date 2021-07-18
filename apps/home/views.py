"""Home views."""


from django.shortcuts import render


# Create your views here.
def home(request):
    """Return home html template."""
    return render(request, "home/home.html")
