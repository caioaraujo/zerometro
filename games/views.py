from django.views.generic import TemplateView, FormView

from .services import GameService


class Games(TemplateView):
    template_name = "games/games.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["lista_games"] = GameService.get_all()
        return context


class GameId(TemplateView):
    template_name = "games/game.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["game"] = GameService.get_by_id(game_id=kwargs["game_id"])
        return context
