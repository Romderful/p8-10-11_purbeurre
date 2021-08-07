from django.urls import path
from .views import home, legal_notice


urlpatterns = [
    path("", home, name="home"),
    path("legal_notice/", legal_notice, name="legal_notice"),
]
