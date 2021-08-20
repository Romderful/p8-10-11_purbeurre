"""Accounts views."""


from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from .forms import CustomUserCreationForm


BACKEND = "apps.accounts.authenticate.EmailAuthenticate"


class SignUpView(CreateView):
    """SignUpView class."""

    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


@login_required
def profile(request):
    """Profile view."""
    return render(request, "pages/profile.html")
