from django.db.models import F, BooleanField, Value

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
            plataforma_nome=F("game__plataforma__nome"),
        )
        if progresso.exists():
            return progresso.first()

        game = Game.objects.filter(id=game_id).values(
            game_nome=F("nome"),
            plataforma_nome=F("plataforma__nome"),
            finalizado=Value(False, output_field=BooleanField()),
            completado=Value(False, output_field=BooleanField()),
            lista_desejos=Value(False, output_field=BooleanField()),
        )
        return game.first()
