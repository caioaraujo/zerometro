from django.test import TestCase
from freezegun import freeze_time
from model_bakery import baker

from ..models import Game


class TestModels(TestCase):
    def setUp(self):
        self.game_finalizado = baker.make(
            "Game",
            id=1,
            nome="Super Mario World",
            plataforma="Super Nintendo",
            finalizado=True,
        )
        self.game_nao_finalizado = baker.make(
            "Game", id=2, nome="Sonic Unleashed", plataforma="Xbox360", finalizado=False
        )

    @freeze_time("2018-01-01 08:45")
    def test_adiciona_game_finalizado(self):
        game = Game()
        game.nome = "Legend of Zelda - Ocarina of Time"
        game.plataforma = "Nintendo 64"
        game.finalizado = True
        game.save()

        self.assertIsNotNone(game.id)
        self.assertEqual(
            "2018-01-01 08:45", game.data_criado.strftime("%Y-%m-%d %H:%M")
        )
        self.assertEqual(
            "2018-01-01 08:45", game.data_alterado.strftime("%Y-%m-%d %H:%M")
        )
        self.assertEqual("Legend of Zelda - Ocarina of Time", game.nome)
        self.assertEqual("Nintendo 64", game.plataforma)
        self.assertTrue(game.finalizado)

    @freeze_time("2018-01-01 08:45")
    def test_adiciona_game_nao_finalizado(self):
        game = Game()
        game.nome = "Donkey Kong Country 2"
        game.plataforma = "Super Nintendo"
        game.finalizado = False
        game.save()

        self.assertIsNotNone(game.id)
        self.assertEqual(
            "2018-01-01 08:45", game.data_criado.strftime("%Y-%m-%d %H:%M")
        )
        self.assertEqual(
            "2018-01-01 08:45", game.data_alterado.strftime("%Y-%m-%d %H:%M")
        )
        self.assertEqual("Donkey Kong Country 2", game.nome)
        self.assertEqual("Super Nintendo", game.plataforma)
        self.assertFalse(game.finalizado)

    @freeze_time("2022-04-05 18:14")
    def test_altera_game(self):
        game = Game.objects.get(id=2)
        data_criado_esperado = game.data_criado
        game.nome = "Sonic Colors"
        game.finalizado = True
        game.save()

        self.assertEqual("Sonic Colors", game.nome)
        self.assertTrue(game.finalizado)
        self.assertEqual(
            "2022-04-05 18:14", game.data_alterado.strftime("%Y-%m-%d %H:%M")
        )
        self.assertEqual(data_criado_esperado, game.data_criado)

    def test_str(self):
        self.assertEqual(
            "Super Mario World - Super Nintendo", str(self.game_finalizado)
        )
