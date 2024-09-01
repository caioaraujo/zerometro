from django.test import TestCase
from freezegun import freeze_time
from model_bakery import baker

from ..models import Game, Plataforma


class TestModels(TestCase):
    def setUp(self):
        self.plataforma_snes = baker.make(
            "Plataforma",
            id=1,
            nome="Super Nintendo",
        )

        self.plataforma_xbox360 = baker.make(
            "Plataforma",
            id=2,
            nome="Xbox360",
        )

        self.plataforma_n64 = baker.make(
            "Plataforma",
            id=3,
            nome="Nintendo 64",
        )

        self.plataforma_jaguar = baker.make(
            "Plataforma",
            id=4,
            nome="Jaguar",
        )

        self.game_finalizado = baker.make(
            "Game",
            id=1,
            nome="Super Mario World",
            plataforma_id=1,
            finalizado=True,
            completado=False,
            midia="DIGITAL",
        )
        self.game_nao_finalizado = baker.make(
            "Game",
            id=2,
            nome="Sonic Unleashed",
            plataforma_id=2,
            finalizado=False,
            completado=False,
            midia="FISICA",
        )

    def test_adiciona_plataforma(self):
        plataforma = Plataforma()
        plataforma.nome = "Playstation 3"
        plataforma.save()

        self.assertIsNotNone(plataforma.id)
        self.assertEqual("Playstation 3", plataforma.nome)

    def test_altera_plataforma(self):
        plataforma = Plataforma.objects.get(id=4)
        plataforma.nome = "Atari Jaguar"
        plataforma.save()

        self.assertEqual("Atari Jaguar", plataforma.nome)

    @freeze_time("2018-01-01 08:45")
    def test_adiciona_game_completado(self):
        game = Game()
        game.nome = "Legend of Zelda - Ocarina of Time"
        game.plataforma_id = 3
        game.finalizado = False
        game.completado = True
        game.lista_desejos = True
        game.save()

        self.assertIsNotNone(game.id)
        self.assertEqual(
            "2018-01-01 08:45", game.data_criado.strftime("%Y-%m-%d %H:%M")
        )
        self.assertEqual(
            "2018-01-01 08:45", game.data_alterado.strftime("%Y-%m-%d %H:%M")
        )
        self.assertEqual("Legend of Zelda - Ocarina of Time", game.nome)
        self.assertEqual("Nintendo 64", game.plataforma.nome)
        self.assertFalse(game.lista_desejos)
        self.assertTrue(game.finalizado)
        self.assertTrue(game.completado)

    @freeze_time("2018-01-01 08:45")
    def test_adiciona_game_finalizado(self):
        game = Game()
        game.nome = "Legend of Zelda - Ocarina of Time"
        game.plataforma_id = 3
        game.finalizado = True
        game.completado = True
        game.lista_desejos = True
        game.save()

        self.assertIsNotNone(game.id)
        self.assertEqual(
            "2018-01-01 08:45", game.data_criado.strftime("%Y-%m-%d %H:%M")
        )
        self.assertEqual(
            "2018-01-01 08:45", game.data_alterado.strftime("%Y-%m-%d %H:%M")
        )
        self.assertEqual("Legend of Zelda - Ocarina of Time", game.nome)
        self.assertEqual("Nintendo 64", game.plataforma.nome)
        self.assertFalse(game.lista_desejos)
        self.assertTrue(game.finalizado)

    @freeze_time("2018-01-01 08:45")
    def test_adiciona_game_lista_desejos(self):
        game = Game()
        game.nome = "Legend of Zelda - Ocarina of Time"
        game.plataforma_id = 3
        game.finalizado = False
        game.completado = False
        game.lista_desejos = True
        game.save()

        self.assertIsNotNone(game.id)
        self.assertEqual(
            "2018-01-01 08:45", game.data_criado.strftime("%Y-%m-%d %H:%M")
        )
        self.assertEqual(
            "2018-01-01 08:45", game.data_alterado.strftime("%Y-%m-%d %H:%M")
        )
        self.assertEqual("Legend of Zelda - Ocarina of Time", game.nome)
        self.assertEqual("Nintendo 64", game.plataforma.nome)
        self.assertTrue(game.lista_desejos)
        self.assertFalse(game.finalizado)
        self.assertFalse(game.completado)

    @freeze_time("2018-01-01 08:45")
    def test_adiciona_game_nao_finalizado(self):
        game = Game()
        game.nome = "Donkey Kong Country 2"
        game.plataforma_id = 1
        game.finalizado = False
        game.completado = False
        game.lista_desejos = False
        game.midia = "DIGITAL"
        game.save()

        self.assertIsNotNone(game.id)
        self.assertEqual(
            "2018-01-01 08:45", game.data_criado.strftime("%Y-%m-%d %H:%M")
        )
        self.assertEqual(
            "2018-01-01 08:45", game.data_alterado.strftime("%Y-%m-%d %H:%M")
        )
        self.assertEqual("Donkey Kong Country 2", game.nome)
        self.assertEqual("Super Nintendo", game.plataforma.nome)
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

    def test_adiciona_plataforma_e_game(self):
        plataforma = Plataforma()
        plataforma.nome = "Master System"
        plataforma.save()

        game = Game()
        game.nome = "California Games"
        game.plataforma_id = plataforma.id
        game.finalizado = False
        game.completado = False
        game.lista_desejos = True
        game.save()

        self.assertEqual(game.plataforma_id, plataforma.id)

    def test_remove_plataforma(self):
        Plataforma.objects.get(id=1).delete()

        with self.assertRaises(Plataforma.DoesNotExist):
            Plataforma.objects.get(id=1)

        # Asserts cascade delete
        with self.assertRaises(Game.DoesNotExist):
            Game.objects.get(plataforma_id=1)

    def test_str(self):
        self.assertEqual(
            "Super Mario World - Super Nintendo", str(self.game_finalizado)
        )
        self.assertEqual("Super Nintendo", str(self.plataforma_snes))
