from django.urls import path
from django.views.generic.base import RedirectView

from . import views

app_name = "game"
urlpatterns = [
    path("", RedirectView.as_view(url="games/", permanent=False), name="index"),
    path("games/", views.Games.as_view(), name="games"),
    path("game/<int:game_id>/", views.GameId.as_view(), name="game"),
]
