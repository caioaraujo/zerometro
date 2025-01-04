from django.contrib.auth.models import User
from django.test import TestCase
from model_bakery import baker


class TestViews(TestCase):
    def setUp(self):
        self.user = baker.make(User)
        baker.make("Game", id=1, nome="Game 1")
        baker.make("Game", _quantity=4)

    def test_get_games(self):
        self.client.force_login(self.user)
        response = self.client.get("/games/", follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(5, response.context["lista_games"].count())

    def test_fetch_game(self):
        self.client.force_login(self.user)
        response = self.client.get("/game/1/", follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual("Game 1", response.context["game"].nome)

    def test_fetch_game_when_user_is_not_logged_in(self):
        response = self.client.get("/game/1/", follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, "/login.html?next=/game/1/")
