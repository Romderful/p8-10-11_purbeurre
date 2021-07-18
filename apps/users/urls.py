"""Users urls."""


from django.urls import path
from .views import sign_in, sign_up, sign_out, profile


urlpatterns = [
    path("signup", sign_up, name="signup"),
    path("signin", sign_in, name="signin"),
    path("signout", sign_out, name="signout"),
    path("profile", profile, name="profile"),
]
