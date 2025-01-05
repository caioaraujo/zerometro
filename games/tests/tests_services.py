from django.contrib.auth.models import User
from django.test import TestCase
from model_bakery import baker

from ..models import Progresso
from ..services import GameService


class TestGameService(TestCase):

    def test_get_all__with_data(self):
        baker.make("Game", 15)

        all_games = GameService.get_all()
        self.assertEqual(15, len(all_games))

    def test_get_all__with_no_data(self):
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
        self.assertEqual("Super Nintendo", result["plataforma_nome"])
        self.assertTrue(result["finalizado"])
        self.assertTrue(result["completado"])
        self.assertFalse(result["lista_desejos"])

    def test_get_game_progresso__when_user_has_no_progresso(self):
        user = baker.make(User)
        user2 = baker.make(User)

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

        result = GameService.get_game_progresso(game.id, user2.id)
        self.assertEqual("Super Mario World", result["game_nome"])
        self.assertEqual("Super Nintendo", result["plataforma_nome"])
        self.assertFalse(result["finalizado"])
        self.assertFalse(result["completado"])
        self.assertFalse(result["lista_desejos"])

    def test_save_progresso__when_user_has_no_progresso(self):
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
        progresso = {"finalizado": True, "completado": True, "lista_desejos": False}
        GameService.save_progresso(progresso, game.id, user.id)

        expected_progresso = Progresso.objects.filter(
            game_id=game.id, user_id=user.id
        ).first()
        self.assertTrue(expected_progresso.finalizado)
        self.assertTrue(expected_progresso.completado)
        self.assertFalse(expected_progresso.lista_desejos)

    def test_save_progresso__when_user_has_progresso(self):
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
            completado=False,
            lista_desejos=False,
        )
        novo_progresso = {
            "finalizado": True,
            "completado": True,
            "lista_desejos": False,
        }
        GameService.save_progresso(novo_progresso, game.id, user.id)

        expected_progresso = Progresso.objects.filter(
            game_id=game.id, user_id=user.id
        ).first()
        self.assertTrue(expected_progresso.finalizado)
        self.assertTrue(expected_progresso.completado)
        self.assertFalse(expected_progresso.lista_desejos)

    def test_save_progresso__when_user_has_no_progresso_and_all_values_is_false(self):
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
        novo_progresso = {
            "finalizado": False,
            "completado": False,
            "lista_desejos": False,
        }
        GameService.save_progresso(novo_progresso, game.id, user.id)

        expected_progresso = Progresso.objects.filter(game_id=game.id, user_id=user.id)
        self.assertFalse(expected_progresso.exists())
