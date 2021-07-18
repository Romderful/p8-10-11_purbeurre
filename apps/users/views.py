"""Users view."""


from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib import auth
from .forms import SignupForm, SigninForm


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
    return render(request, "signup.html", context)


def sign_in(request):
    """Sign in view."""
    form = SigninForm()
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.error(request, "Identifiant ou mot de passe invalide :(.")
            return redirect("/account/signin")
    context = {"form": form}
    return render(request, "signin.html", context)


def sign_out(request):
    """Sign out view."""
    auth.logout(request)
    return redirect("/")
