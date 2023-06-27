from .models import Game


class GameService:

    def get_all(self):
        return Game.objects.all()
