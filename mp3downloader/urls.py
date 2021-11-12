from django.urls import path

from .views import mp3

urlpatterns = [
    path("", mp3, name="homepage"),
]
