from django.urls import path
from .views import sign_in, log_in


urlpatterns = [
    path("signin", sign_in, name="sign_in"),
    path("login", log_in, name="log_in"),
]
