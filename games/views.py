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
        progresso = GameService.get_game_progresso(
            game_id=kwargs["game_id"], user_id=self.request.user.id
        )
        context["game"] = progresso["game_nome"]
        context["plataforma"] = progresso["plataforma_nome"]
        context["finalizado"] = progresso["finalizado"]
        context["completado"] = progresso["completado"]
        context["lista_desejos"] = progresso["lista_desejos"]
        return context
