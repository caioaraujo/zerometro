from django.test import TestCase
from freezegun import freeze_time
from model_bakery import baker

from ..models import Game, Plataforma, Progresso


class TestModels(TestCase):
    def setUp(self):
        self.plataforma_snes = baker.make(
            "Plataforma",
            # id=1,
            nome="Super Nintendo",
        )
        self.plataforma_xbox360 = baker.make(
            "Plataforma",
            # id=2,
            nome="Xbox360",
        )
        self.plataforma_n64 = baker.make(
            "Plataforma",
            # id=3,
            nome="Nintendo 64",
        )
        self.plataforma_jaguar = baker.make(
            "Plataforma",
            # id=4,
            nome="Jaguar",
        )
        self.game_1 = baker.make(
            "Game",
            nome="Super Mario World",
            plataforma_id=self.plataforma_snes.id,
            midia="DIGITAL",
        )
        self.game_2 = baker.make(
            "Game",
            nome="Legend of Zelda Ocarina of Time",
            plataforma_id=self.plataforma_n64.id,
            midia="DIGITAL",
        )
        self.game_3 = baker.make(
            "Game",
            nome="Red Dead Redemption",
            plataforma_id=self.plataforma_xbox360.id,
            midia="FISICA",
        )
        self.user_1 = baker.make(
            "auth.User",
        )

    def test_adiciona_plataforma(self):
        plataforma = Plataforma()
        plataforma.nome = "Playstation 3"
        plataforma.save()

        self.assertIsNotNone(plataforma.id)
        self.assertEqual("Playstation 3", plataforma.nome)

    def test_altera_plataforma(self):
        plataforma = Plataforma.objects.get(id=self.plataforma_jaguar.id)
        plataforma.nome = "Atari Jaguar"
        plataforma.save()

        self.assertEqual("Atari Jaguar", plataforma.nome)

    @freeze_time("2018-01-01 08:45")
    def test_adiciona_game(self):
        game = Game()
        game.nome = "Legend of Zelda - Ocarina of Time"
        game.plataforma_id = self.plataforma_n64.id
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

    @freeze_time("2022-04-05 18:14")
    def test_altera_game(self):
        game = Game.objects.get(id=self.game_2.id)
        data_criado_esperado = game.data_criado
        game.nome = "Sonic Colors"
        game.save()

        self.assertEqual("Sonic Colors", game.nome)
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
        game.save()

        self.assertEqual(game.plataforma_id, plataforma.id)

    def test_remove_plataforma(self):
        Plataforma.objects.get(id=self.plataforma_snes.id).delete()

        with self.assertRaises(Plataforma.DoesNotExist):
            Plataforma.objects.get(id=self.plataforma_snes.id)

        # Asserts cascade delete
        with self.assertRaises(Game.DoesNotExist):
            Game.objects.get(plataforma_id=self.plataforma_snes.id)

    def test_str(self):
        self.assertEqual("Super Mario World - Super Nintendo", str(self.game_1))
        self.assertEqual("Super Nintendo", str(self.plataforma_snes))

    def test_adiciona_progresso(self):
        progresso_finalizado = Progresso()
        progresso_finalizado.game_id = self.game_1.id
        progresso_finalizado.user_id = self.user_1.id
        progresso_finalizado.finalizado = True
        progresso_finalizado.completado = False
        progresso_finalizado.lista_desejos = True
        progresso_finalizado.save()

        self.assertTrue(progresso_finalizado.finalizado)
        self.assertFalse(progresso_finalizado.completado)
        self.assertFalse(progresso_finalizado.lista_desejos)

        progresso_completado = Progresso()
        progresso_completado.game_id = self.game_2.id
        progresso_completado.user_id = self.user_1.id
        progresso_completado.finalizado = False
        progresso_completado.completado = True
        progresso_completado.lista_desejos = False
        progresso_completado.save()

        self.assertTrue(progresso_completado.finalizado)
        self.assertTrue(progresso_completado.completado)
        self.assertFalse(progresso_completado.lista_desejos)

        progresso_lista_desejos = Progresso()
        progresso_lista_desejos.game_id = self.game_3.id
        progresso_lista_desejos.user_id = self.user_1.id
        progresso_lista_desejos.finalizado = False
        progresso_lista_desejos.completado = False
        progresso_lista_desejos.lista_desejos = True
        progresso_lista_desejos.save()

        self.assertFalse(progresso_lista_desejos.finalizado)
        self.assertFalse(progresso_lista_desejos.completado)
        self.assertTrue(progresso_lista_desejos.lista_desejos)
