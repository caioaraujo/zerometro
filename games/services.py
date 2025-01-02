from .models import Game


class GameService:

    @staticmethod
    def get_all():
        return Game.objects.all()

    @staticmethod
    def get_by_id(game_id):
        return Game.objects.get(id=game_id)
