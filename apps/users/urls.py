"""Users urls."""


from django.urls import path
from .views import sign_in, sign_up


urlpatterns = [
    path("signup", sign_up, name="signup"),
    path("signin", sign_in, name="signin"),
]
