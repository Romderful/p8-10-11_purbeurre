"""Accounts models."""


from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    """Class User."""

    USERNAME_FIELD = "email"
    email = models.EmailField(_("Adresse email"), unique=True)
    REQUIRED_FIELDS = ["username"]
