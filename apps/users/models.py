"""Users models."""


from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """Class User."""

    email = models.EmailField(_("user_email"), blank=False, unique=True)
