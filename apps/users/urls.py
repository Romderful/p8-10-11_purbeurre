"""Users urls."""


from django.urls import path
from .views import sign_in, sign_up, sign_out, profile


urlpatterns = [
    path("sign_up", sign_up, name="sign_up"),
    path("sign_in", sign_in, name="sign_in"),
    path("sign_out", sign_out, name="sign_out"),
    path("profile", profile, name="profile"),
]
