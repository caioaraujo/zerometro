from django.contrib.auth.models import User
from django.test import TestCase
from model_bakery import baker


class TestViews(TestCase):
    def setUp(self):
        self.user = baker.make(User)
        self.user2 = baker.make(User)
        plataforma = baker.make("Plataforma", id=1, nome="Plataforma 1")
        game = baker.make("Game", id=1, nome="Game 1", plataforma=plataforma)
        baker.make("Game", _quantity=4)
        baker.make(
            "Progresso",
            user_id=self.user.id,
            game_id=game.id,
            finalizado=True,
            completado=False,
            lista_desejos=False,
        )

    def test_get_games(self):
        self.client.force_login(self.user)
        response = self.client.get("/games/", follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(5, response.context["lista_games"].count())

    def test_fetch_game(self):
        self.client.force_login(self.user)
        response = self.client.get("/game/1/", follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual("Game 1", response.context["game"])
        self.assertEqual("Plataforma 1", response.context["plataforma"])
        self.assertTrue(response.context["finalizado"])
        self.assertFalse(response.context["completado"])
        self.assertFalse(response.context["lista_desejos"])

    def test_fetch_game__when_user_has_no_progresso(self):
        self.client.force_login(self.user2)
        response = self.client.get("/game/1/", follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual("Game 1", response.context["game"])
        self.assertEqual("Plataforma 1", response.context["plataforma"])
        self.assertFalse(response.context["finalizado"])
        self.assertFalse(response.context["completado"])
        self.assertFalse(response.context["lista_desejos"])

    def test_fetch_game__when_user_is_not_logged_in(self):
        response = self.client.get("/game/1/", follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertIsNone(response.context.get("game"))
        self.assertRedirects(response, "/login.html?next=/game/1/")
