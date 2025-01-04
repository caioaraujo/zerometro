from django.db.models import F

from .models import Game, Progresso


class GameService:

    @staticmethod
    def get_all():
        return Game.objects.all()

    @staticmethod
    def get_game_progresso(game_id, user_id):
        progresso = Progresso.objects.filter(user_id=user_id, game_id=game_id).values(
            "finalizado",
            "completado",
            "lista_desejos",
            game_nome=F("game__nome"),
            plataforma=F("game__plataforma__nome"),
        )
        return progresso.first()
