from django.urls import path

from . import views

app_name = "catalog"
urlpatterns = [
    path("games/", views.Games.as_view(), name="games"),
    path("game/<int:game_id>/", views.GameId.as_view(), name="game"),
]
