from django.shortcuts import render


# Create your views here.
def sign_in(request):
    """Sign in view."""
    return render(request, "signin.html")


def log_in(request):
    """Sign in view."""
    return render(request, "login.html")
