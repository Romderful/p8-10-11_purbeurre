"""Users views."""


from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm


BACKEND = "apps.users.authenticate.EmailAuthenticate"


# Create your views here.
def sign_up(request):
    """Return sign up html template."""
    form = SignupForm()
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid() and form.clean_email():
            form.save()
            return redirect("/")
    context = {"form": form}
    return render(request, "users/signup.html", context)


def sign_in(request):
    """Sign in view."""
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            messages.error(request, "Identifiant ou mot de passe invalide :(.")
            return redirect("/users/sign_in")
    return render(request, "users/signin.html")


def sign_out(request):
    """Sign out view."""
    logout(request)
    return redirect("/")


def profile(request):
    """Profile view."""
    if not request.user.is_authenticated:
        return redirect("/users/sign_in")
    return render(request, "users/profile.html")
