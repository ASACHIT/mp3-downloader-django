from django.urls import path

from .views import AudioView, HomeView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("mp3", AudioView, name="audio_listing"),
]
