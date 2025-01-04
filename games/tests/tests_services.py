from django.contrib.auth.models import User
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

    def test_get_game_progresso(self):
        user = baker.make(User)

        plataforma = baker.make(
            "Plataforma",
            nome="Super Nintendo",
        )

        game = baker.make(
            "Game",
            nome="Super Mario World",
            plataforma_id=plataforma.id,
            midia="DIGITAL",
        )

        baker.make(
            "Progresso",
            game=game,
            user=user,
            finalizado=True,
            completado=True,
            lista_desejos=False,
        )

        result = GameService.get_game_progresso(game.id, user.id)
        self.assertEqual("Super Mario World", result["game_nome"])
        self.assertEqual("Super Nintendo", result["plataforma"])
        self.assertTrue(result["finalizado"])
        self.assertTrue(result["completado"])
        self.assertFalse(result["lista_desejos"])
