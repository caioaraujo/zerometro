from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, FormView

from .forms import GameForm
from .services import GameService


class Games(TemplateView):
    template_name = "games/games.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["lista_games"] = GameService.get_all()
        return context


class GameId(LoginRequiredMixin, FormView, TemplateView):
    form_class = GameForm
    login_url = "login:login_view"
    template_name = "games/game.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["game"] = GameService.get_by_id(game_id=kwargs["game_id"])
        return context
