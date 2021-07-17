"""Users view."""


from django.shortcuts import render
from .forms import SignupForm


# Create your views here.
def sign_up(request):
    """Return sign up html template."""
    form = SignupForm()
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid() and form.clean_email():
            form.save()
    context = {"form": form}
    return render(request, "signup.html", context)


def sign_in(request):
    """Sign in view."""
    return render(request, "signin.html")
