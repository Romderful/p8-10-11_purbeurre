"""Accounts forms."""


from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """CustomUserCreationForm class."""

    class Meta(UserCreationForm):
        """Meta class."""

        model = CustomUser
        fields = UserCreationForm.Meta.fields
        fields = ("username", "email")


class CustomUserChangeForm(UserChangeForm):
    """CustomUserChangeForm class."""

    class Meta:
        """Meta class."""

        model = CustomUser
        fields = UserChangeForm.Meta.fields
        fields = ("username", "email")
