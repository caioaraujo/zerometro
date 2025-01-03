from django.test import TestCase
from model_bakery import baker

from ..services import GameService


class TestGameService(TestCase):

    def test_get_all_with_data(self):
        baker.make("Game", 15)

        all_games = GameService.get_all()
        self.assertEqual(15, len(all_games))

    def test_get_all_with_no_data(self):
        all_games = GameService.get_all()
        self.assertEqual(0, len(all_games))

    def test_get_by_id(self):
        baker.make(
            "Plataforma",
            id=1,
            nome="Super Nintendo",
        )

        baker.make(
            "Game",
            id=1,
            nome="Super Mario World",
            plataforma_id=1,
            midia="DIGITAL",
        )

        game = GameService.get_by_id(1)
        self.assertEqual("Super Mario World", game.nome)
