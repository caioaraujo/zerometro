from django.views.generic import TemplateView

from .services import GameService


class Games(TemplateView):
    template_name = "games/games.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["lista_games"] = GameService.get_all()
        return context
